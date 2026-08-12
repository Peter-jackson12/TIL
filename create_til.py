import datetime
from pathlib import Path

# 1. 오늘 배운 datetime 모듈로 오늘 날짜 구하기 ('2026-08-12' 형식)
today_str = datetime.datetime.now().strftime("%Y-%m-%d")

# 2. TIL 폴더 생성 (없으면 자동 생성)
til_dir = Path(__file__).resolve().parent / "TIL"
til_dir.mkdir(exist_ok=True)

# 3. 오늘 날짜를 파일명으로 지정 (예: TIL/2026-08-12.md)
file_path = til_dir / f"{today_str}.md"

# 4. 오늘 날짜가 자동으로 박히는 마크다운 템플릿
markdown_content = f"""# 📝 Today I Learned (TIL)

> **날짜:** {today_str}  
> **작성자:** 개발자  

---

## 💡 오늘 배운 핵심 내용
- 

## 🛠️ 코드 실습 및 트러블슈팅
```python
# 코드 작성
```"""

# 5. 파일 생성 및 내용 쓰기
file_path.write_text(markdown_content, encoding='utf-8')
