# 📚 Data Science & AI Bootcamp — TIL & Devlog

> 9.5개월간의 데이터 사이언스 & AI 서비스 개발 과정을 기록하는 개발 일지(Devlog) 저장소입니다.  
> 수업에서 배운 내용, 궁금했던 질문, 직접 해본 실험과 해결 과정을 기록합니다. 개념을 이해한 날은 짧은 TIL로, 프로젝트 문제를 해결한 날은 자세한 Devlog로 남깁니다.

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
├── README.md                 # 사용 안내 및 학습 기록 목차
├── template.md               # 학습 자료를 TIL로 정리하는 요청문
├── create_til.py             # 빈 TIL 양식 생성 (선택 사항)
├── main.py                   # 기존 브랜치 연습 파일
├── 2026-08/                  # YYYY-MM-DD.md 형식의 일별 기록
└── 2026-09/
```

---

## 📑 학습 기록 목차

| 날짜 | 단계 | 대표 주제 및 실무 해결 내용 | 마크다운 링크 |
| :---: | :---: | :--- | :---: |
| **2026-08-05** | AI | 생성형 AI·LLM, 프롬프트 구성 및 책임 있는 AI 활용 | [📄 보기](./2026-08/2026-08-05.md) |
| **2026-08-06** | Git / Python | 브랜치·병합·Rebase·충돌, uv 환경 및 주피터 연동 | [📄 보기](./2026-08/2026-08-06.md) |
| **2026-08-07** | Python | 변수·자료형·형변환·연산자·f-string 및 실습 질문 | [📄 보기](./2026-08/2026-08-07.md) |
| **2026-08-10** | Python / Tools | 딕셔너리·집합·조건문, 개발 환경 및 프로젝트 기획 | [📄 보기](./2026-08/2026-08-10.md) |
| **2026-08-11** | Python | 반복문·함수·매개변수, 데이터프레임 및 개발 생태계 | [📄 보기](./2026-08/2026-08-11.md) |
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
| **2026-08-31** | Stats / SQL / DevOps | 통계학 수리 증명(이항분포 분산 $np(1-p)$·자유도 $n-1$ 베셀 보정), IEEE 754 극단값 SF, Python `set` 해시 비결정론, PostgreSQL 스키마 파이프라인 | [📄 보기](./2026-08/2026-08-31.md) |
| **2026-09-01** | ML / OR / DevOps | ML 분류 모델 파이프라인(Logistic vs LightGBM), 마케팅 임계값(Threshold) 비즈니스 최적화, OR 최적화 이론 연계, Cline + 로컬 Ollama 우회 연동 | [📄 보기](./2026-09/2026-09-01.md) |
| **2026-09-02** | ML / Algo / Quant | 이분 탐색과 B+Tree 인덱스 연계, 원-핫 인코딩과 경사하강법 수리 증명, OLS 정규방정식(SSE) 구현, RTX 5060 환경 및 KIS End-to-End 퀀트 아키텍처 | [📄 보기](./2026-09/2026-09-02.md) |
| **2026-09-04** | ML / Stats / Quant | 선형·로지스틱 회귀 엔진(OLS vs GD vs LP), L1/L2 정규화 및 GridSearchCV 튜닝, 분류 지표의 역설(기상청 CSI 실증), 퀀트 시계열 초단타 누수(Leakage) 방어 | [📄 보기](./2026-09/2026-09-04.md) |
| **2026-09-07** | ML / OOP / Quant | OOP 인스턴스 메모리 수명주기(`self`), 분류 평가지표 역설(혼동행렬·조화평균 F1·ROC-AUC), CART 동점 분기·외삽 한계, 트리 앙상블과 퀀트 유니버스 커팅 | [📄 보기](./2026-09/2026-09-07.md) |
| **2026-09-08** | ML / Data / Quant | 100만 행 불균형 분류 6단계 진화(Threshold 0.22 튜닝·비대칭 Pseudo-Labeling 8.9만 건 증강·시간 역산 복원), K-Means 거리 왜곡·PCA 수리 증명(Cov=Corr), SQL 옵티마이저 CBO 사이클, KIS WebSocket 및 1초봉 LOB 51컬럼 수집기 | [📄 보기](./2026-09/2026-09-08.md) |
| **2026-09-10** | SQL / Quant / Infra | RDBMS CBO 옵티마이저·실행계획(EXPLAIN) 해석, B-Tree 인덱스 vs 인메모리 Hash Join 메커니즘, 다단계 JOIN 체인과 1:N 행 팽창 검증, `LEFT JOIN`의 `ON` vs `WHERE` 필터링 위치와 Anti-Join 무결성 검증, 키움증권 Open API+ 32비트 격리 가상환경 구축 | [📄 보기](./2026-09/2026-09-10.md) |
| **2026-09-11** | SQL / Quant / Microstructure | PostgreSQL 윈도우 함수 딥다이브(GROUP BY 대비 행 보존성, 순위 3종·NTILE 사분위수, 프레임 이동평균·LAG/LEAD, CBO WindowAgg/Sort 내부 구조), 키움 Open API+ 32비트 2,550개 보통주 전 종목 무차별 틱 수집기, FID 14 결손 대응 Lee-Ready 호가 대조 알고리즘, 1초봉 한계(스프레드 -0.395%) 극복 및 순수 틱 백테스터 구현 | [📄 보기](./2026-09/2026-09-11.md) |
| **2026-09-14** | Stats / SQL / ML / Quant | 가설검정 수리 증명($p$-value 귀류법·$\alpha$-$\beta$ 시소·동등성 검정 TOST), PostgreSQL `EXPLAIN ANALYZE` 병렬 스캔 정밀 계측(`loops=3`), 항공 지연 ML 외부 기상 결합 사후 부검(Post-Mortem: AUC 0.59 급락과 피처 오염 메커니즘), 퀀트 Architecture V2 런·피처 스토어 패리티 파이프라인 구축 | [📄 보기](./2026-09/2026-09-14.md) |
| **2026-09-15** | Stats / ML / Quant / AI DevOps | 가설검정 실질적 유의성(Cohen's d vs $p$-value)·Levene 등분산 알고리즘 수리 해체, Ames Housing 주피터 범용 파이프라인, 항공 지연 ML 조기종료(ES) 병리 부검과 트리 50그루 고정 역전(AUC 0.6451), 퀀트 틱 수집 데몬 무인 검증 및 AI 에이전트 150k 토큰 다이어트 | [📄 보기](./2026-09/2026-09-15.md) |
| **2026-09-16** | Stats / Algo / ML / Quant | 통계 검정·Pearson·OLS 수리 이해, 항공 지연 OOF·결측 오류 분석, 틱 수집 컨트롤 타워 구현 및 검증 | [📄 보기](./2026-09/2026-09-16.md) |
| **2026-09-17** | Stats / A-B Test / Quant | Pearson·단순회귀 $R^2$ 수리 연결, Cookie Cats A/B 랜덤화·SRM 진단과 MDE-Power 표본설계, Stock NXT venue 판정·크래시 대응·구독 계획 구현(커밋 확인) 및 실규모 병목 우선순위 판단, Airplane Carrier 식별자·BTS 연도 후보 압축 | [📄 보기](./2026-09/2026-09-17.md) |

---

## 💡 학습 및 작성 원칙

1. **배운 만큼 기록하기:** 질문 하나를 이해한 날도 TIL로 남깁니다. 실험이나 트러블슈팅이 없는 날은 해당 항목을 생략합니다.
2. **사실과 추측 구분하기:** 직접 실행한 결과, AI가 제안한 예시, 아직 확인하지 않은 가설을 구분합니다. 제공되지 않은 수치나 경험을 만들어 넣지 않습니다.
3. **다시 이해할 수 있게 쓰기:** 중요한 질문, 코드, 오류 메시지, 실행 조건, 출처를 보존합니다. 특정 실험의 결과를 보편적 결론으로 단정하지 않습니다.
4. **간결하게 유지하기:** 주제 요약은 한 줄로 적고, 퀀트 연결이나 거창한 성과 표현을 의무화하지 않습니다. 기존 기록은 당시 형식을 유지합니다.

## ✍️ 하루 기록 흐름

### 1. 수업과 질문

일반 ChatGPT에서 수업 내용, 개념 질문, 자유로운 질의응답을 진행합니다. 저장소 파일을 직접 읽거나 실행해야 하는 작업은 해당 프로젝트에서 진행합니다.

### 2. 하루 마무리 요약

학습한 대화에서 아래 요청문을 사용합니다. 대화가 여러 개라면 각 요약을 모읍니다.

```text
오늘 대화에서 TIL에 남길 학습 내용을 주제별로 정리해줘.
내가 한 질문, 이해한 답, 직접 실행한 코드와 결과, 미해결 질문을 보존해줘.
AI가 제안한 코드와 내가 실제 실행한 코드를 구분하고,
중요한 수치·오류 메시지·출처를 남겨줘.
실행하지 않은 실험이나 확인하지 않은 결론은 만들지 마.
```

### 3. 이 저장소에서 TIL 작성

[작성 요청 템플릿](./template.md)에 학습 날짜를 지정하고, 요약과 중요한 코드·로그 원문을 붙여 넣습니다. 다른 대화의 내용을 이미 알고 있다고 가정하지 않고 필요한 자료를 함께 전달합니다.

TIL 파일을 작성한 뒤 위 목차에 날짜·주제·링크를 추가합니다. 같은 날짜가 있으면 기존 내용을 보완하고 목차 행은 중복 생성하지 않습니다. 날짜별 설명은 목차 한 곳에서 관리합니다.

기본 양식은 아래와 같습니다. 내용이 없는 항목은 생략하고 번호를 맞춥니다.

- 오늘 배운 것
- 내가 궁금했던 질문과 이해한 답
- 직접 해본 것과 결과 — 실행한 경우에만
- 아직 헷갈리는 것 / 다음에 확인할 것

프로젝트 문제 해결이 중심인 날에는 기존의 **문제 → 실험 → 해결 → 배운 점** 형식을 사용해도 됩니다.

## 🛠️ 빈 양식 생성 (선택 사항)

AI에게 파일 작성을 맡길 때는 스크립트를 먼저 실행할 필요가 없습니다. 직접 작성할 빈 양식이 필요할 때 저장소 루트에서 실행합니다.

```powershell
# 오늘 날짜 (컴퓨터의 로컬 날짜)
python create_til.py

# 지난 학습 내용을 나중에 정리할 때
python create_til.py 2026-09-15
```

Python 3.10 이상과 표준 라이브러리만 사용합니다. Python 명령이 등록되지 않았다면 설치된 인터프리터 경로로 실행합니다. 이 저장소에 사용 가능한 가상환경이 있다면 다음과 같이 실행할 수 있습니다.

```powershell
.\.venv\Scripts\python.exe create_til.py 2026-09-15
```

스크립트는 월별 폴더와 빈 마크다운 파일만 생성하며, 기존 파일은 덮어쓰지 않습니다. AI 호출, 내용 정리, README 목차 갱신은 수행하지 않습니다.
