import pandas as pd

if __name__ == "__main__":
    train_path = "dataset/train.csv"
    House_data = pd.read_csv(train_path)
    print(House_data)