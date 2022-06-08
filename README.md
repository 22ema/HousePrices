# HousePrices
study HousePrices in kaggle

# 대회의 목적
집값을 정확하게 예측하는 것이 목표
평가 기준 : RMSLE
RMSLE를 사용하는 이유는 목적변수 집값의 범위가 넓기 때문이다.

# 데이터 탐색
- 변수가 많고 Train과 Test 데이터의 사이즈가 비슷하기 때문에 Cross Validation과 Feature Selection이 필요함
- 데이터 내에 Object가 53%로 가장 많은 것을 알 수 있다. 그래서 적절한 Encoding 기법을 선택하는 것이 중요

# environment
pandas 1.1.5
matplotlib 3.3.4
scikit-learn 0.24.2
numpy 1.19.5

# 사용 방법
python run.py