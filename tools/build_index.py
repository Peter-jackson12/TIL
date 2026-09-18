"""학습 기록 파일에서 목차를 만들어 낸다.

각 기록 파일의 머리말에 적힌 날짜·단계·주제를 읽어서 세 가지를 생성한다.

1. 저장소 README의 월별 요약표 (표시 구간 사이만 교체한다)
2. 월 폴더마다 그 달의 일별 목차 파일
3. 주제별 색인 파일

목차를 손으로 고치지 않기 위한 도구다. 기록 파일이 유일한 원본이고 목차는
그로부터 다시 만들어지므로, 같은 설명을 두 곳에 적어 두고 서로 어긋나는 일이
생기지 않는다.

사용법:
    python tools/build_index.py           # 목차 파일을 새로 쓴다
    python tools/build_index.py --check   # 쓰지 않고 최신 상태인지만 확인한다

초기 형식으로 쓴 기록은 머리말 구성이 지금과 달라 본문을 건드리지 않는다.
그 기록들의 목차 정보는 tools/legacy_index.tsv 에 따로 보존하며, 이 도구가
두 출처를 합쳐 하나의 목차를 만든다.
"""

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
LEGACY_FILE = BASE / "tools" / "legacy_index.tsv"
TOPICS_FILE = BASE / "docs" / "topics.md"
INDEX_BEGIN = "<!-- 목차 시작: tools/build_index.py 가 생성합니다. 직접 고치지 마세요. -->"
INDEX_END = "<!-- 목차 끝 -->"
SUBJECT_LIMIT = 90


def read_entries():
    """기록 파일과 초기 형식 표를 합쳐 날짜순으로 돌려준다."""
    legacy = {}
    if LEGACY_FILE.exists():
        for line in LEGACY_FILE.read_text(encoding="utf-8").splitlines():
            if not line.strip() or line.startswith("#"):
                continue
            date, stage, subject = (line.split("\t") + ["", ""])[:3]
            legacy[date.strip()] = (stage.strip(), subject.strip())

    entries, missing = [], []
    for path in sorted(BASE.glob("2026-*/2026-*.md")):
        date = path.stem
        text = path.read_text(encoding="utf-8-sig")
        stage = find_field(text, "단계")
        subject = find_field(text, "주제")

        if not (stage and subject) and date in legacy:
            stage, subject = legacy[date]
        if not (stage and subject):
            missing.append(date)
            continue

        entries.append({
            "date": date,
            "month": date[:7],
            "stage": stage,
            "subject": subject,
            "path": path,
        })
    return entries, missing


def find_field(text, name):
    """머리말에서 `> **이름:** 값` 한 줄을 찾아 값만 돌려준다."""
    match = re.search(rf"^>\s*\*\*{name}:\*\*\s*(.+?)\s*(?:<br>)?\s*$", text, re.M)
    return match.group(1).strip() if match else ""


def split_tags(stage):
    """`Stats / ML / Quant` 같은 표기를 개별 주제로 나눈다."""
    return [tag.strip() for tag in re.split(r"[/·]", stage) if tag.strip()]


def shorten(subject):
    return subject if len(subject) <= SUBJECT_LIMIT else subject[:SUBJECT_LIMIT - 1].rstrip() + "…"


def render_readme_index(entries):
    by_month = defaultdict(list)
    for entry in entries:
        by_month[entry["month"]].append(entry)

    lines = [
        f"| 월 | 기록 | 주요 단계 | 월별 목차 |",
        "| :---: | :---: | :--- | :---: |",
    ]
    for month in sorted(by_month):
        group = by_month[month]
        tags = Counter(tag for entry in group for tag in split_tags(entry["stage"]))
        top = " · ".join(tag for tag, _ in tags.most_common(4))
        lines.append(f"| **{month}** | {len(group)}건 | {top} | [열기](./{month}/README.md) |")
    lines.append("")
    lines.append(f"기록 {len(entries)}건. 날짜를 모를 때는 [주제별 색인](./docs/topics.md)에서 찾습니다.")
    return "\n".join(lines)


def render_month_index(month, group):
    lines = [
        f"# {month} 학습 기록",
        "",
        f"이 달의 기록 {len(group)}건입니다. 전체 목차는 [저장소 README](../README.md)에 있습니다.",
        "",
        "| 날짜 | 단계 | 주제 | 기록 |",
        "| :---: | :---: | :--- | :---: |",
    ]
    for entry in group:
        lines.append(
            f"| **{entry['date'][8:]}일** | {entry['stage']} | "
            f"{shorten(entry['subject'])} | [보기](./{entry['date']}.md) |"
        )
    lines.append("")
    return "\n".join(lines)


def render_topics(entries):
    topics = defaultdict(list)
    for entry in entries:
        for tag in split_tags(entry["stage"]):
            topics[tag].append(entry)

    lines = [
        "# 주제별 색인",
        "",
        "날짜를 기억하지 못해도 주제로 기록을 찾을 수 있게 만든 색인입니다.",
        "각 기록 머리말의 단계 표기에서 자동으로 생성하므로 직접 고치지 않습니다.",
        "",
    ]
    for tag in sorted(topics, key=lambda t: (-len(topics[t]), t)):
        group = topics[tag]
        links = " · ".join(
            f"[{e['date'][5:]}](../{e['month']}/{e['date']}.md)" for e in group
        )
        lines.append(f"### {tag} ({len(group)}건)")
        lines.append("")
        lines.append(links)
        lines.append("")
    return "\n".join(lines)


def replace_index_block(readme_text, block):
    """README의 표시 구간 사이만 새 목차로 바꾼다."""
    pattern = re.compile(
        re.escape(INDEX_BEGIN) + r".*?" + re.escape(INDEX_END),
        re.S,
    )
    replacement = f"{INDEX_BEGIN}\n\n{block}\n\n{INDEX_END}"
    if not pattern.search(readme_text):
        raise SystemExit(
            "README에서 목차 표시 구간을 찾지 못했습니다.\n"
            f"다음 두 줄을 목차 자리에 넣어 주세요.\n\n{INDEX_BEGIN}\n{INDEX_END}"
        )
    return pattern.sub(replacement, readme_text)


def write_if_changed(path, content, check_only, stale):
    current = path.read_text(encoding="utf-8") if path.exists() else None
    if current == content:
        return False
    if check_only:
        stale.append(path.relative_to(BASE).as_posix())
        return True
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="파일을 쓰지 않고 목차가 최신인지만 확인한다")
    check_only = parser.parse_args().check

    entries, missing = read_entries()
    if missing:
        print("머리말에 단계 또는 주제가 없고 초기 형식 표에도 없는 기록이 있습니다:",
              file=sys.stderr)
        for date in missing:
            print(f"  {date}", file=sys.stderr)
        return 1
    if not entries:
        print("기록 파일을 찾지 못했습니다.", file=sys.stderr)
        return 1

    stale, changed = [], []

    readme_path = BASE / "README.md"
    new_readme = replace_index_block(
        readme_path.read_text(encoding="utf-8"), render_readme_index(entries)
    )
    if write_if_changed(readme_path, new_readme, check_only, stale):
        changed.append("README.md")

    by_month = defaultdict(list)
    for entry in entries:
        by_month[entry["month"]].append(entry)
    for month, group in sorted(by_month.items()):
        path = BASE / month / "README.md"
        if write_if_changed(path, render_month_index(month, group), check_only, stale):
            changed.append(f"{month}/README.md")

    if write_if_changed(TOPICS_FILE, render_topics(entries), check_only, stale):
        changed.append("docs/topics.md")

    if check_only:
        if stale:
            print("목차가 기록과 다릅니다. python tools/build_index.py 를 실행하세요.",
                  file=sys.stderr)
            for name in stale:
                print(f"  {name}", file=sys.stderr)
            return 1
        print(f"목차가 최신입니다. 기록 {len(entries)}건.")
        return 0

    print(f"기록 {len(entries)}건으로 목차를 만들었습니다.")
    for name in changed:
        print(f"  갱신: {name}")
    if not changed:
        print("  바뀐 내용 없음")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
