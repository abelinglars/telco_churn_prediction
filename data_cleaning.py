# This script will clean the data and write the resulting frame as csv to /data directory
import sys
from abc import ABC, abstractmethod

import numpy as np
import pandas as pd

class Loader(ABC):
    """Data Loaders Interface"""
    @abstractmethod
    def load(self, source: str) -> pd.DataFrame:
        pass

class CSVLoader(Loader):
    """Load csv files"""
    def __init__(self, source:str):
        self.source = source
    def load(self, source: str) -> pd.DataFrame:
        return pd.read_csv(source)

class TelcoCleaner():
    def __init__(self, path: str):
        self.path = path
        self.data:pd.DataFrame = pd.DataFrame()

    def load_data(self, source, loader):
        loader = loader(source)
        self.data = loader.load(self.path)

    def validate_input(self):
        pass

    def clean_column_names(self):

        clean_column_names = [
          "customer_id",
          "gender",
          "senior_citizen",
          "partner",
          "dependents",
          "tenure",
          "phone_service",
          "multiple_lines",
          "internet_service",
          "online_security",
          "online_backup",
          "device_protection",
          "tech_support",
          "streaming_tv",
          "streaming_movies",
          "contract",
          "paperless_billing",
          "payment_method",
          "monthly_charges",
          "total_charges",
          "churn"
        ]

        renaming_dict = {}

        for old, new in zip(self.data.columns.values, clean_column_names):
          renaming_dict[old] = new

        self.data = self.data.rename(columns = renaming_dict)

    def fix_total_charges(self):
        """ 
        Total charges is missing for rows where tenure == 0. We impute the value with the value
        of monthy_charges assuming that they paid for the first month but the data hasnt updated.
        Converts the 'total_charges to float'.
        """

        # find empty total charges values
        empty_values = self.data[
            "total_charges"
        ][self.data["total_charges"].isin(
            [" ", ""]
        )].index.values

        # find columns where tenure == 0
        zero_tenure = self.data.loc[self.data['tenure'] == 0].index.values

        if not np.array_equal(empty_values, zero_tenure):
            raise Exception

        # impute monthly into total charges
        self.data.loc[
            self.data['tenure'] == 0,
            'total_charges'
        ] = self.data.loc[self.data['tenure'] == 0, 'monthly_charges']


        # now all values should be numeric
        self.data['total_charges'] = pd.to_numeric(self.data['total_charges'], errors = "coerce")

    def check_string_cols_for_empty_values(self):
        string_cols = self.data.select_dtypes(include = "object")
        out = 0
        for col in string_cols:
            out += self.data[col].isin(["", " "]).sum()

        if out > 0:
            raise Exception

    def remove_columns(self):
        self.data = self.data.drop(columns = "customer_id")

    def validate_output(self):
        pass

    def preprocess_data(self):
        pass

    def is_cleaned(self):
        pass

    def show(self):
        if self.data is None:
            print(f"No data instantiated. Load data first.")
        else:
            print(f"{self.data.shape}")
            print(self.data.info())




if __name__ == "__main__":
    if len(sys.argv) == 1:
        path = sys.argv[1]
    else:
        path = "raw_data/raw_data_telco.csv"
    cleaner = TelcoCleaner(path)
    cleaner.load_data(source = path, loader = CSVLoader)
    cleaner.clean_column_names()
    cleaner.fix_total_charges()
    cleaner.check_string_cols_for_empty_values()
    cleaner.show()
