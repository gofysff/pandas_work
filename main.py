import pandas as pd


def load_data():
    return pd.read_excel('assets/lab1_air_pollution.xlsx', index_col=0)


if __name__ == '__main__':
    data_df = load_data()

    print(data_df['Population'])
