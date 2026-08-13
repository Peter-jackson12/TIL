# 📚 Data Science & AI Bootcamp — TIL & Devlog

> 9.5개월간의 데이터 사이언스 & AI 서비스 개발 과정을 기록하는 개발 일지(Devlog) 저장소입니다.  
> 단순한 강의 내용 복사가 아닌, **직면한 문제(Problem), 직접 검증한 코드(Experiment), 해결 과정(Solution)** 중심의 인사이트를 기록합니다.

---

## 🛠️ Main Tech Stack & Tools

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square&logo=python&logoColor=white) ![uv](https://img.shields.io/badge/Package_Manager-uv-DE5B43?style=flat-square&logo=rust&logoColor=white) ![VS Code](https://img.shields.io/badge/IDE-VS_Code-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white) ![Git](https://img.shields.io/badge/VCS-Git-F05032?style=flat-square&logo=git&logoColor=white) ![Pandas](https://img.shields.io/badge/Data-Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)

---

## 📂 저장소 구조 (Repository Architecture)

```text
.
├── README.md                 # TIL 저장소 안내 및 목차
├── template.md               # AI 기반 Devlog 작성 템플릿
├── create_til.py             # 일일 TIL 자동 생성 스크립트
└── 2026-08/                  # 2026년 8월 학습 기록
    └── 2026-08-12.md         # 변수 스코프, uv 패키지 관리, 퀀트 엔진 모듈화
        └── 2026-08-13.md         # 예외 처리, 비주얼 디버거, OOP 클래스, 퀀트 엔진 디버깅
📑 핵심 학습 및 리팩토링 하이라이트 (Milestones)
날짜	단계	대표 주제 및 실무 해결 내용	마크다운 링크
2026-08-12	Python	600줄 퀀트 백테스팅 엔진 7모듈 리팩토링, uv 의존성 도입, 한글 인코딩(utf-8-sig) 해결	📄 보기
2026-08-13	Python / OOP	예외 처리(try-except), 비주얼 디버거(Debug Cell), 클래스(OOP), 퀀트 엔진 디버깅 및 한글 종목명 매핑	📄 보기
💡 학습 및 작성 원칙 (Writing Principles)
문제 해결 중심 (Problem-Solving): 코드를 짜며 겪은 에러, 버그, 의구심을 기록하고 이를 직접 주피터 노트북에서 검증한 결과를 적습니다.
현대적 개발 환경 준수: 모든 프로젝트 환경은 Rust 기반 uv 패키지 매니저(pyproject.toml, uv.lock)를 적극 도입하여 재현성을 보장합니다.
지속 가능한 성장 (Consistency): 커리큘럼이 진행됨에 따라 단단해지는 소프트웨어 아키텍처 및 데이터 엔지니어링 역량을 기록합니다.
🤖 AI Devlog Generator
이 저장소는 template.md에 정의된 프롬프트를 기반으로 일일 학습 및 트러블슈팅 내역을 정밀한 Devlog형 마크다운 문서로 변환하여 관리합니다.
---