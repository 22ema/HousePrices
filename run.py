import pandas as pd
from utils.dataengineering import DataEngineering
from utils.make_graph import MakeGraph

def make_bivariate_graph(MG, df, y_axis):
    count = 1
    save_path = "ResultGraph/"
    graph_name = ""
    for df_index in df.columns[:-1]:
        if count == 5:
            count = 1
            MG.save_graph(save_path + graph_name + ".png")
            MG.clear_graph()
            graph_name = ""
        graph_name += df_index + "_"
        MG.bivariate_graph(df_index, y_axis, 4, count)
        count += 1



if __name__ == "__main__":
    train_path = "dataset/train.csv"
    House_data = pd.read_csv(train_path)
    DE = DataEngineering(House_data)
    House_data = DE.label_encoder()
    MG = MakeGraph(House_data)
    make_bivariate_graph(MG, House_data, 'SalePrice')