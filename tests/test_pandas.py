"""This is the starting test file"""
import random
from pprint import pprint

import pandas
import pandas as pd
from pathlib import Path

from app.file_ops import FileOperations


def test_pandas():
    """testing pandas"""
    data_absolute_path = FileOperations.get_calculate_file_path(Config.population_data_directory,
                                                                Config.population_data_file_name)
    df = pd.read_csv(data_absolute_path)

    random.randint(0, 9)
    print(df.to_string())
    # print(df.shape[0])
    # pprint(df.loc[4])
    record = df.loc[df['state'] == "Montana"]
    print(record)
    mean = PandasMean.result(df, "pop")
    print(mean)
    min = PandasMin.get_min_from_df(df, "pop")
    print(min)
    std = PandasStdDev.get_std_dev_from_df(df, "pop")
    print(std)

    records = pandas.DataFrame()
    records.append(df.loc[df['state'] == "Montana"])


class PandasMean:
    @staticmethod
    def result(data_frame: pandas.DataFrame, field_name: str):
        return data_frame[field_name].mean()


class PandasStdDev:
    @staticmethod
    def get_std_dev_from_df(data_frame: pandas.DataFrame, field_name: str):
        return data_frame[field_name].std()


class PandasMin:
    @staticmethod
    def get_min_from_df(data_frame: pandas.DataFrame, field_name: str):
        return data_frame[field_name].min()


class Config:
    population_data_directory = "data"
    population_data_file_name = "state_population.csv"
