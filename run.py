import csv
import numpy as np
import pandas as pd
import os
from utils.dataengineering import DataEngineering
from utils.make_graph import MakeGraph
from model.Multi_Regression import MultiRegression

def make_bivariate_graph(MG, df, y_axis):
    '''
    make a bivariate graph about the SalePrice and the others
    :param MG: MaaeGraph instance
    :param df: dataframe
    :param y_axis: target value
    '''
    count = 1
    save_path = "ResultGraph/"
    graph_name = ""
    for df_index in df.columns[:-1]:
        if count == 5:
            count = 1
            graph_img_name = graph_name + ".png"
            if graph_img_name in os.listdir(save_path):
                pass
            else:
                MG.save_graph(save_path + graph_img_name)
            MG.clear_graph()
            graph_name = ""
        graph_name += df_index + "_"
        MG.bivariate_graph(df_index, y_axis, 4, count)
        count += 1

def corr_csv(corr, path):
    corr_column = corr.columns
    corr_value = np.array(corr)
    with open(path, 'w', newline='') as file:
        mywriter = csv.writer(file, delimiter=',')
        mywriter.writerow(corr_column)
        for i in corr_value:
            mywriter.writerow(i)

def make_result_csv(index, preds):
    result = [[0] * 2 for _ in range(0, len(index))]
    idx = ['Id', 'SalePrice']
    for i in range(0, len(index)):
        result[i][0] = index[i]
        result[i][1] = preds[i]
    df = pd.DataFrame(result, columns=idx)
    df.to_csv('./csv/result.csv', index=False)




if __name__ == "__main__":
    # make train dataset for Multi Regression(ML)
    train_path = "dataset/train.csv"
    House_data = pd.read_csv(train_path)
    DE = DataEngineering(House_data)
    House_data = DE.label_encoder()
    DE.check_missing_value()
    DE.fill_missing_value('ffill')
    MG = MakeGraph(House_data)
    make_bivariate_graph(MG, House_data, 'SalePrice')
    corr = DE.corr_coef()
    if 'corr_data.csv' in os.listdir('./csv'):
        pass
    else:
        corr_csv(corr, 'csv/corr_data.csv')
    train_x = np.asarray(DE.dataframe[House_data.columns[1:-1]])
    train_y = np.asarray(DE.dataframe[House_data.columns[-1]])

    # make test dataset
    test_path = "dataset/test.csv"
    tHouse_data = pd.read_csv(test_path)
    tDE = DataEngineering(tHouse_data)
    tHouse_data = tDE.label_encoder()
    tDE.check_missing_value()
    tDE.fill_missing_value('ffill')
    index = np.asarray(tDE.dataframe[tHouse_data.columns[0]])
    test_x = np.asarray(tDE.dataframe[tHouse_data.columns[1:]])

    # Multi Regression
    mregr = MultiRegression(train_x, train_y)
    mregr.fit_reg()
    preds = mregr.prediction(test_x)
    make_result_csv(index, preds)
