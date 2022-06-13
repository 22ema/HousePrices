
import xgboost as XGB
import numpy as np
from sklearn.metrics import mean_squared_error

class XGBModel():

    def __init__(self, x, y):
        self.model = XGB.XGBRegressor(colsample_bytree=0.4603, gamma=0.0468,
                             learning_rate=0.05, max_depth=3,
                             min_child_weight=1.7817, n_estimators=2200,
                             reg_alpha=0.4640, reg_lambda=0.8571,
                             subsample=0.5213, random_state =7, nthread = -1)
        self.x = x
        self.y = y

    def fit_reg(self):
        self.model.fit(self.x, self.y)

    def prediction(self, test_x):
        pred = self.model.predict(test_x)
        pred = np.floor(np.expm1(pred))
        return pred

    def matrix_print(self, test_y, test_x, pred):
        print("Residual sum of squares : %.2f"%np.mean((pred-test_y)**2))
        print("Variance score: %.2f" % self.regr.score(test_x, test_y))
        print("RMSE : %.2f" % mean_squared_error(test_y, pred, Squared=False))