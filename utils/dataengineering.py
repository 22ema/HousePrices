from sklearn.preprocessing import LabelEncoder

class DataEngineering():

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def label_encoder(self):
        '''
        Convert object type to int type
        :return: self.dataframe
        '''
        le = LabelEncoder()
        for i in self.dataframe:
            if self.dataframe[i].dtype == 'object':
                self.dataframe[i] = le.fit_transform(self.dataframe[i])
        return self.dataframe

    def check_missing_value(self):
        '''
        check the missing value in the dataframe and print the missing value number
        '''
        missing_num_cnt = self.dataframe.isnull().sum()
        print("missing number's count :", sum(missing_num_cnt))

    def fill_missing_value(self, method):
        '''
        using method for fill missing value
        :return:
        '''
        self.dataframe = self.dataframe.fillna(method=method)

    def corr_coef(self):
        '''
        make a correlation coefficient matrix
        :return: corr matrix
        '''
        corr = self.dataframe.corr()
        return corr