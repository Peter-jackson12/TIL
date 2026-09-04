# 📚 Data Science & AI Bootcamp — TIL & Devlog

> 9.5개월간의 데이터 사이언스 & AI 서비스 개발 과정을 기록하는 개발 일지(Devlog) 저장소입니다.  
> 단순한 강의 내용 복사가 아닌, **직면한 문제(Problem), 직접 검증한 코드(Experiment), 해결 과정(Solution)** 중심의 실전 인사이트를 기록합니다.

---

## 🛠️ Main Tech Stack & Tools

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square&logo=python&logoColor=white) 
![uv](https://img.shields.io/badge/Package_Manager-uv-DE5B43?style=flat-square&logo=rust&logoColor=white) 
![VS Code](https://img.shields.io/badge/IDE-VS_Code-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white) 
![Git](https://img.shields.io/badge/VCS-Git-F05032?style=flat-square&logo=git&logoColor=white) 
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![DBeaver](https://img.shields.io/badge/Tool-DBeaver-372923?style=flat-square&logo=dbeaver&logoColor=white)
![Pandas](https://img.shields.io/badge/Data-Pandas-150458?style=flat-square&logo=pandas&logoColor=white) 
![SciPy](https://img.shields.io/badge/Stats-SciPy-8CAAE6?style=flat-square&logo=scipy&logoColor=white)
![Scikit_Learn](https://img.shields.io/badge/ML-Scikit_Learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![Streamlit](https://img.shields.io/badge/App-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Viz-Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)
![Ollama](https://img.shields.io/badge/Local_AI-Ollama-black?style=flat-square&logo=ollama&logoColor=white)

---

## 📂 저장소 구조 (Repository Architecture)

```text
.
├── README.md                 # TIL 저장소 안내 및 전체 목차
├── template.md               # AI 기반 Devlog 작성 템플릿
├── create_til.py             # 일일 TIL 자동 생성 스크립트
├── 2026-08/                  # 2026년 8월 학습 기록
│   ├── 2026-08-12.md         # 변수 스코프, uv 패키지 관리, 퀀트 엔진 모듈화
│   ├── 2026-08-13.md         # 예외 처리, 비주얼 디버거, OOP 클래스, 퀀트 엔진 디버깅
│   ├── 2026-08-14.md         # OOP 매직 메서드(__str__), iloc[0] 파이프라인 인덱싱, 연산 최적화
│   ├── 2026-08-18.md         # 파일 I/O(JSON/CSV), Matplotlib 한글화, RDBMS 구조 및 600MB DB 샘플링
│   ├── 2026-08-19.md         # RDBMS 정규화·ERD, PostgreSQL/DBeaver 파이프라인, 퀀트 대시보드 연동
│   ├── 2026-08-20.md         # SQL 쿼리 라이프사이클(WHERE/HAVING/JOIN), 퀀트 올인원 저장소 통합(Phase 2)
│   ├── 2026-08-24.md         # Pandas 내부 메커니즘(iloc/loc), 순수 Python OOP 파이프라인, SQL 서브쿼리
│   ├── 2026-08-25.md         # Pandas 다중 집계(agg/pivot), rrule 시계열, EDA 이상치 분석, LEFT JOIN 무결성
│   ├── 2026-08-27.md         # Matplotlib/Seaborn OOP, AI 에이전트(Cline/MCP/Ollama), KRX 70만 행 이상치 탐지
│   ├── 2026-08-28.md         # KRX 전처리 파이프라인, Day & Night Anomaly(Overnight Alpha), 자유도·베이즈 정리
│   └── 2026-08-31.md         # 통계학 수리 증명(이항분포 분산·자유도), IEEE 754 극단값 SF, PostgreSQL 스키마
└── 2026-09/                  # 2026년 9월 학습 기록
    ├── 2026-09-01.md         # ML 분류 파이프라인, Threshold 최적화, OR 최적화 이론, Cline 로컬 연동
    └── 2026-09-02.md         # 이분 탐색·B+Tree 인덱스, 원-핫 인코딩 수리 증명, OLS 정규방정식, KIS 퀀트
    └── 2026-09-04.md         # 회귀·분류 엔진(OLS/GD/BCE), L1/L2 정규화·CV 튜닝, 분류 지표의 역설(기상청 CSI), 시계열 누수 방어    
```

---

## 📑 핵심 학습 및 리팩토링 하이라이트 (Milestones)

| 날짜 | 단계 | 대표 주제 및 실무 해결 내용 | 마크다운 링크 |
| :---: | :---: | :--- | :---: |
| **2026-08-12** | Python | 600줄 퀀트 백테스팅 엔진 7모듈 리팩토링, `uv` 의존성 도입, 한글 인코딩(`utf-8-sig`) 해결 | [📄 보기](./2026-08/2026-08-12.md) |
| **2026-08-13** | Python / OOP | 예외 처리(`try-except`), 비주얼 디버거(`Debug Cell`), 클래스(`OOP`), 퀀트 엔진 디버깅 및 한글 종목명 매핑 | [📄 보기](./2026-08/2026-08-13.md) |
| **2026-08-14** | Python / OOP | OOP 매직 메서드(`__str__`), `iloc[0]` 파이프라인 인덱싱, 조건식 단락 평가 최적화, Git Detached HEAD 복구 | [📄 보기](./2026-08/2026-08-14.md) |
| **2026-08-18** | Python / SQL | 파일 I/O(JSON/CSV), Matplotlib 한글화 최적화, `.venv` 경로 복구, RDBMS 구조 및 600MB DB 샘플링 파이프라인 | [📄 보기](./2026-08/2026-08-18.md) |
| **2026-08-19** | SQL / Quant | RDBMS 데이터 무결성·정규화(1NF~3NF)·ERD, PostgreSQL/DBeaver 데이터 파이프라인, Streamlit 퀀트 대시보드 및 로컬 Ollama AI 연동 | [📄 보기](./2026-08/2026-08-19.md) |
| **2026-08-20** | SQL / Quant | SQL 논리적 실행 순서 및 `WHERE` vs `HAVING` 서브쿼리 등가성 검증, `UNION`/`JOIN` 참조 무결성 분석, Stock 퀀트 플랫폼 모노레포 물리 통합(Phase 2) | [📄 보기](./2026-08/2026-08-20.md) |
| **2026-08-24** | Python / SQL | Pandas 내부 메커니즘(`iloc`/`loc`, Boolean Indexing), 순수 Python OOP 파이프라인(`CarSale` 상속/오버라이딩), SQL 서브쿼리 3대 패턴, `uv` 한글 패키지명 트러블슈팅 | [📄 보기](./2026-08/2026-08-24.md) |
| **2026-08-25** | Pandas / EDA / SQL | Pandas 다중 집계(`agg`/`pivot_table`), `str.split`/`rrule` 시계열 생성, Git 스냅샷 원리, EDA 이상치(IQR vs 도메인) 분석, SQL `LEFT JOIN` 무결성 검증 | [📄 보기](./2026-08/2026-08-25.md) |
| **2026-08-27** | Python / Viz / AI | Python 3.14 시각화(Matplotlib/Seaborn OOP), AI 에이전트(Cline/MCP/Gemini 429 쿨다운), KRX 주식 70만 행 도메인 무결성 및 1:N 명칭 노이즈 탐지 엔진 | [📄 보기](./2026-08/2026-08-27.md) |
| **2026-08-28** | Quant / Stats | KRX 70만 행 전처리 파이프라인 완성, Day & Night Anomaly(Overnight Alpha) 실증, 통계학 자유도($df$)와 베이즈 정리의 본질, Git 100MB 파일 제한 복구 | [📄 보기](./2026-08/2026-08-28.md) |
| **2026-08-31** | Stats / SQL / DevOps | 통계학 수리 증명(이항분포 분산 $np(1-p)$·자유도 $n-1$ 베셀 보정), IEEE 754 부동소수점 극단값 $\text{SF}$ 연산, Python `set` 해시 비결정론, PostgreSQL 스키마 파이프라인 | [📄 보기](./2026-08/2026-08-31.md) |
| **2026-09-01** | ML / OR / DevOps | ML 분류 모델 파이프라인(Logistic vs LightGBM), 마케팅 임계값(Threshold) 비즈니스 최적화, OR 최적화 이론 연계, Cline + 로컬 Ollama 우회 연동 | [📄 보기](./2026-09/2026-09-01.md) |
| **2026-09-02** | ML / Algo / Quant | 이분 탐색과 B+Tree 인덱스 연계, 원-핫 인코딩과 경사하강법 수리 증명, OLS 정규방정식(SSE) 구현, RTX 5060 환경 및 KIS End-to-End 퀀트 아키텍처 | [📄 보기](./2026-09/2026-09-02.md) |
| **2026-09-04** | ML / Stats / Quant | 선형·로지스틱 회귀 엔진(OLS vs GD vs LP), L1/L2 정규화 및 GridSearchCV 튜닝, 분류 지표의 역설(기상청 강수적중률 CSI 실증), 퀀트 시계열 초단타 누수(Leakage) 방어 | [📄 보기](./2026-09/2026-09-03.md) |
---

## 💡 학습 및 작성 원칙 (Writing Principles)

1. **문제 해결 중심 (Problem-Solving):** 코드를 짜며 겪은 에러, 버그, 의구심을 기록하고 이를 직접 주피터 노트북과 SQL 엔진에서 검증한 결과를 적습니다.
2. **현대적 개발 환경 준수:** 모든 프로젝트 환경은 Rust 기반 `uv` 패키지 매니저(`pyproject.toml`, `uv.lock`)를 적극 도입하여 재현성을 보장합니다.
3. **지속 가능한 성장 (Consistency):** 커리큘럼이 진행됨에 따라 단단해지는 소프트웨어 아키텍처, 데이터 엔지니어링, 퀀트 시스템 역량을 기록합니다.

---

## 🤖 AI Devlog Generator

이 저장소는 `template.md`에 정의된 프롬프트를 기반으로 일일 학습 및 트러블슈팅 내역을 정밀한 Devlog형 마크다운 문서로 변환하여 관리합니다.
