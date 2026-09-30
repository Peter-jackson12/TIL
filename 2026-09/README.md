# 2026-09 학습 기록

[전체 목차](../README.md#learning-log) · [주제별 색인](../docs/topics.md) · [← 2026-08](../2026-08/README.md)

이 달의 기록 23건입니다. 날짜를 누르면 기록을 읽을 수 있습니다.

| 날짜 | 단계 | 주제 |
| :---: | :--- | :--- |
| [**01일**](./2026-09-01.md) | ML / OR / DevOps | ML 파이프라인(Logistic Regression vs LightGBM), 분류 임계값(Threshold) 최적화, OR(운영연구) 기반 최적화, Cline-… |
| [**02일**](./2026-09-02.md) | ML / Algo / Quant | 이분 탐색(Binary Search)과 DB 인덱스(B+Tree), 원-핫 인코딩과 경사하강법의 수리적 결합, OLS 회귀식 증명(SSE vs 잔차합), RTX… |
| [**04일**](./2026-09-04.md) | ML / Stats / Quant | 선형·로지스틱 회귀 학습 엔진(OLS vs GD vs LP), 정규화(L1/L2)와 하이퍼파라미터 튜닝(GridSearchCV), 분류 평가지표의 역설(기상청… |
| [**07일**](./2026-09-07.md) | ML / OOP / Quant | OOP 인스턴스 메모리 수명주기, 분류 평가지표의 본질(혼동행렬·조화평균 F1·ROC-AUC 줄세우기), CART 동점(Tie) 분기와 외삽 한계, 트리 앙상블… |
| [**08일**](./2026-09-08.md) | ML / Data / Quant | 100만 행 불균형 분류 6단계 진화(Threshold 0.22 튜닝·비대칭 Pseudo-Labeling 8.9만 건 증강·시간 역산 복원), K-Means 거… |
| [**10일**](./2026-09-10.md) | SQL / Quant / Infra | RDBMS CBO 옵티마이저·실행계획(EXPLAIN) 해석, B-Tree 인덱스 vs 인메모리 Hash Join 메커니즘, 다단계 JOIN 체인과 1:N 행 팽… |
| [**11일**](./2026-09-11.md) | SQL / Quant / Microstructure | PostgreSQL 윈도우 함수 딥다이브(GROUP BY 대비 행 보존성, 순위 3종·NTILE 사분위수, 프레임 이동평균·LAG/LEAD, CBO Window… |
| [**14일**](./2026-09-14.md) | Stats / SQL / ML / Quant | 가설검정 수리 증명($p$-value 귀류법·$\alpha$-$\beta$ 시소·동등성 검정 TOST), PostgreSQL `EXPLAIN ANALYZE` 병… |
| [**15일**](./2026-09-15.md) | Stats / ML / Quant / AI DevOps | 가설검정 실질적 유의성(Cohen's d vs $p$-value)·Levene 등분산 알고리즘 수리 해체, Ames Housing 주피터 범용 파이프라인, 항공… |
| [**16일**](./2026-09-16.md) | Stats / Algo / ML / Quant | 통계 검정·Pearson·OLS 수리 이해, 항공 지연 OOF·결측 오류 분석, 틱 수집 컨트롤 타워 구현 및 검증 |
| [**17일**](./2026-09-17.md) | Stats / A-B Test / Quant | Pearson·단순회귀 $R^2$ 수리 연결, Cookie Cats A/B 랜덤화·SRM 진단과 MDE-Power 표본설계, Stock NXT venue 판정·… |
| [**18일**](./2026-09-18.md) | Stats / Product Analytics / Quant / Data Engineering | 확률·통계에서 프로덕트 분석(KPI·AARRR·Funnel·A/B 표본설계)으로 전환, Airplane 우선순위 공항 20곳의 공항-관측소 매핑을 NOAA HO… |
| [**20일**](./2026-09-20.md) | Quant / Data Engineering / DevOps / AI DevOps | Stock 실데이터 후보 선정 보류와 clean 세션 우선 결정, Airplane Git-only/로컬 검증 분리·날씨 수집 재개 예산 계약, GitHub 플러… |
| [**21일**](./2026-09-21.md) | Product Analytics / Stats / ML / Quant / Data Engineering / DevOps | 리텐션·퍼널·A/B 실험 설계와 Ridge/Lasso 복습, product_2 과제 검토, Stock/Airplane 운영 안정화 |
| [**22일**](./2026-09-22.md) | Product Analytics / Stats / ML / Quant / Data Engineering / DevOps / AI DevOps | 프로덕트 분석 문제정의·퍼널/리텐션·A/B 실험 설계, Stock/Airplane 검증, career-agent 근거 기반 자동화 |
| [**23일**](./2026-09-23.md) | ML / Stats | ML 기초부터 시계열·규제·불균형·앙상블·SHAP·하이퍼파라미터 튜닝 복습, Career System 상태 정리 |
| [**24일**](./2026-09-24.md) | Quant / Data Engineering / DevOps / AI DevOps | Stock 포트폴리오·bounded prefix·frozen snapshot 안전 경계, Career System 검증·profile snapshot |
| [**25일**](./2026-09-25.md) | Quant / Data Engineering / DevOps / AI DevOps | Fast Backtest v1·Operator 실행 준비, Career matcher v2·daily operator 전환 |
| [**26일**](./2026-09-26.md) | Quant / Data Engineering / DevOps / AI DevOps | MWFD-04 전체 실행·파이프라인 감사 remediation, Career Tavily·출처 provenance 계약 |
| [**27일**](./2026-09-27.md) | Quant / Data Engineering / DevOps / AI DevOps | MWFD Stage C/D·dual collector smoke, Career eligibility v2·Practical Fit shadow 검증 |
| [**28일**](./2026-09-28.md) | Quant / Data Engineering / DevOps / AI DevOps | MWFD Stage E·강제청산 검증·KRX/NXT dual 수집, Career Hub 통합 |
| [**29일**](./2026-09-29.md) | ML / Stats / Quant / Data Engineering / DevOps / AI DevOps | 모델 선택·시계열 정상성, Stock 체결 트리거 호가 스냅샷, Career Hub intake·Markdown Intake 계획 |
| [**30일**](./2026-09-30.md) | ML / Stats / DevOps | 정상성·ADF·ARIMA의 p·d·q, 예측 검증의 경계와 Career Agent 복구·Hub 표시 개선 |
