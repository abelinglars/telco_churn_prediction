# This script will clean the data and write the resulting frame as csv to /data directory
import sys
import pandas as pd
from abc import ABC, abstractmethod

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
        self.data = None

    def load_data(self, source, loader):
        loader = loader(source)
        self.data = loader.load(self.path)

    def show(self):
        if self.data is None:
            print(f"No data instantiated. Load data first.")
        else:
            print(f"{self.data.shape}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        path = sys.argv[1]
    else:
        path = "raw_data/raw_data_telco.csv"
    cleaner = TelcoCleaner(path)
    cleaner.load_data(source = path, loader = CSVLoader)
    cleaner.show()
    # cleaner.clean_data()
    # cleaner.save_cleaned_data()
