"""학습 날짜의 빈 TIL 양식을 생성한다. 기존 파일은 덮어쓰지 않는다.

머리말의 단계와 주제는 목차 생성에 쓰이므로 비워 두지 않는다.
내용을 채운 뒤 tools/build_index.py 를 실행하면 목차가 갱신된다.
"""

import argparse
from datetime import date
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "date", nargs="?", type=date.fromisoformat, default=date.today(),
        help="학습 날짜 YYYY-MM-DD (생략하면 컴퓨터의 오늘 날짜)",
    )
    learning_date = parser.parse_args().date
    base_dir = Path(__file__).resolve().parent
    target_dir = base_dir / learning_date.strftime("%Y-%m")
    target_dir.mkdir(exist_ok=True)
    file_path = target_dir / f"{learning_date.isoformat()}.md"

    content = f"""# 📝 Today I Learned (TIL)

> **날짜:** {learning_date.isoformat()}<br>
> **작성자:** Peter-jackson12<br>
> **단계:**<br>
> **주제:**

<!-- 내용이 없는 항목은 삭제하고 번호를 맞춥니다. 실제 실행과 예시, 관찰과 추측을 구분합니다. -->

## 1. 오늘 배운 것

-

## 2. 내가 궁금했던 질문과 이해한 답

- **질문:**
- **이해한 답:**

## 3. 직접 해본 것과 결과

<!-- 직접 실행한 경우에만 코드·조건·결과를 기록합니다. -->

-

## 4. 아직 헷갈리는 것 / 다음에 확인할 것

-
"""
    try:
        with file_path.open("x", encoding="utf-8", newline="\n") as output:
            output.write(content)
    except FileExistsError:
        print(f"[이미 존재함] {file_path.relative_to(base_dir)}")
    else:
        print(f"[생성 완료] {file_path.relative_to(base_dir)}")


if __name__ == "__main__":
    main()
