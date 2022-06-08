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