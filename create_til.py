import datetime
from pathlib import Path

# 1. 오늘 날짜 및 년-월 구하기
now = datetime.datetime.now()
today_str = now.strftime("%Y-%m-%d")
month_str = now.strftime("%Y-%m")

# 2. 프로젝트 루트 폴더 기준 '월별 폴더' 생성 (예: TIL/2026-03/)
BASE_DIR = Path(__file__).resolve().parent
target_dir = BASE_DIR / month_str
target_dir.mkdir(exist_ok=True)

# 3. 마크다운 파일 경로 설정 (예: TIL/2026-03/2026-03-31.md)
file_path = target_dir / f"{today_str}.md"

# 4. Devlog 포맷으로 통일된 마크다운 템플릿
header = f"# 📝 Today I Learned (TIL)\n\n> **날짜:** {today_str}\n> **작성자:** Peter-jackson12\n\n---\n\n"
body = (
    "## 1. 문제 인식 (Problem Recognition)\n"
    "* \n\n"
    "## 2. 직접 코드 실험 (Direct Code Experiment)\n"
    "```python\n"
    "# 실험 및 검증 코드 작성\n"
    "```\n\n"
    "## 3. 트러블슈팅 및 해결 (Troubleshooting & Resolution)\n"
    "### Issue 1: \n"
    "* **원인:** \n"
    "* **해결:** \n\n"
    "---\n"
    "### Key Takeaways\n"
    "1. \n"
)

markdown_content = header + body

# 5. 파일 생성 (utf-8-sig 적용으로 VS Code/한글 깨짐 차단)
if not file_path.exists():
    with open(file_path, "w", encoding="utf-8-sig") as f:
        f.write(markdown_content)
    print(f"✅ [생성 완료] {file_path.relative_to(BASE_DIR)}")
else:
    print(f"⚠️ [이미 존재함] {file_path.relative_to(BASE_DIR)}")