"""This is the starting test file"""
import os
import random
from pprint import pprint

import pandas as pd
from pathlib import Path


def test_pandas():
    """testing pandas"""
    project_root_path = os.getcwd()
    data_directory = "data"
    data_file_name = "state_population.csv"
    data_absolute_path = os.path.join(project_root_path, data_directory, data_file_name)
    df = pd.read_csv(data_absolute_path)

    random.randint(0, 9)
    # print(df.to_string())
    print(df.shape[0])
    pprint(df.loc[4])
