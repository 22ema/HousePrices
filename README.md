# HousePrices
study HousePrices in kaggle

# 대회의 목적
집값을 정확하게 예측하는 것이 목표
평가 기준 : RMSLE
RMSLE를 사용하는 이유는 목적변수 집값의 범위가 넓기 때문이다.

# 데이터 탐색
- 변수가 많고 Train과 Test 데이터의 사이즈가 비슷하기 때문에 Cross Validation과 Feature Selection이 필요함
- 데이터 내에 Object가 53%로 가장 많은 것을 알 수 있다. 그래서 적절한 Encoding 기법을 선택하는 것이 중요

# 데이터 해석
- MSSubClass : 판매와 관련된 주거 유형 식별
-       20	1-STORY 1946 & NEWER ALL STYLES
        30	1-STORY 1945 & OLDER
        40	1-STORY W/FINISHED ATTIC ALL AGES
        45	1-1/2 STORY - UNFINISHED ALL AGES
        50	1-1/2 STORY FINISHED ALL AGES
        60	2-STORY 1946 & NEWER
        70	2-STORY 1945 & OLDER
        75	2-1/2 STORY ALL AGES
        80	SPLIT OR MULTI-LEVEL
        85	SPLIT FOYER
        90	DUPLEX - ALL STYLES AND AGES
       120	1-STORY PUD (Planned Unit Development) - 1946 & NEWER
       150	1-1/2 STORY PUD - ALL AGES
       160	2-STORY PUD - 1946 & NEWER
       180	PUD - MULTILEVEL - INCL SPLIT LEV/FOYER
       190	2 FAMILY CONVERSION - ALL STYLES AND AGES
- MSZoning : 판매의 일반 구역 분류를 식별
-      A	Agriculture
       C	Commercial
       FV	Floating Village Residential
       I	Industrial
       RH	Residential High Density
       RL	Residential Low Density
       RP	Residential Low Density Park 
       RM	Residential Medium Density
- LotFrontage : 부동산에 연결된 거리의 직선 feet(거리)
- LotArea : Lot 크기  (제곱피트)
- Street : 부동산 근처 도로 유형
-      Grvl	Gravel	
       Pave	Paved
- Alley : 부동산 근처 골목 유형
-      Grvl	Gravel
       Pave	Paved
       NA 	No alley access
- LotShape : 부동산 일반적인 형태
-      Reg	Regular	
       IR1	Slightly irregular
       IR2	Moderately Irregular
       IR3	Irregular
- LandContour : 부동산의 평탄 정도
-      Lvl	Near Flat/Level	
       Bnk	Banked - Quick and significant rise from street grade to building
       HLS	Hillside - Significant slope from side to side
       Low	Depression
- Utilities : 사용 가능한 유틸리티 유형
-      AllPub	All public Utilities (E,G,W,& S)	
       NoSewr	Electricity, Gas, and Water (Septic Tank)
       NoSeWa	Electricity and Gas Only
       ELO	Electricity only
- LotConfig : Lot 설정(구성?)
-      Inside	Inside lot
       Corner	Corner lot
       CulDSac	Cul-de-sac
       FR2	Frontage on 2 sides of property
       FR3	Frontage on 3 sides of property