import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
class MultiRegression():

    def __init__(self, x, y):
        self.regr = linear_model.LinearRegression()
        self.x = x
        self.y = y

    def fit_reg(self):
        self.regr.fit(self.x, self.y)

    def prediction(self, test_x):
        pred = self.regr.predict(test_x)
        pred = np.floor(np.expm1(pred))
        return pred

    def matrix_print(self, test_y, test_x, pred):
        print("Residual sum of squares : %.2f"%np.mean((pred-test_y)**2))
        print("Variance score: %.2f" % self.regr.score(test_x, test_y))
        print("RMSE : %.2f" % mean_squared_error(test_y, pred, Squared=False))

