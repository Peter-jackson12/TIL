import datetime
from pathlib import Path

# 1. 오늘 날짜 및 년-월 구하기
now = datetime.datetime.now()
today_str = now.strftime("%Y-%m-%d")    # 예: '2026-08-12'
month_str = now.strftime("%Y-%m")       # 예: '2026-08'

# 2. 프로젝트 루트 폴더 기준 바로 아래에 '월별 폴더' 생성 (예: TIL/2026-08/)
BASE_DIR = Path(__file__).resolve().parent
target_dir = BASE_DIR / month_str
target_dir.mkdir(exist_ok=True)

# 3. 마크다운 파일 경로 설정 (예: TIL/2026-08/2026-08-12.md)
file_path = target_dir / f"{today_str}.md"

# 4. 마크다운 템플릿 내용 (안전한 분리 조합 방식)
header = f"# 📝 Today I Learned (TIL)\n\n> **날짜:** {today_str}\n> **작성자:** 개발자\n\n---\n\n"
body = "## 💡 오늘 배운 핵심 내용\n- \n\n## 🛠️ 코드 실습 및 트러블슈팅\n```python\n# 코드 작성\n```\n\n## 🎯 오늘의 회고 (Retrospective)\n- **Keep:** \n- **Problem:** \n- **Try:** \n"

markdown_content = header + body

# 5. 파일 생성 (이미 존재하면 덮어쓰지 않음)
if not file_path.exists():
    with open(file_path, "w", encoding="utf-8-sig") as f:
        f.write(markdown_content)
    print(f"✅ [생성 완료] {file_path.relative_to(BASE_DIR)}")
else:
    print(f"⚠️ [이미 존재함] {file_path.relative_to(BASE_DIR)}")