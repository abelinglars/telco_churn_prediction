# load libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from data_cleaning import CSVLoader


class DataPrep():
    def __init__(self, data: pd.DataFrame):
        self.data  = data

    def object_to_int(self, col):
        if col.dtype == "object":
            col = LabelEncoder().fit_transform(y = col)
        return col

    def label_encode_cols(self):
        self.data = self.data.apply(
          lambda x: self.object_to_int(x)
        )
            
    def get_data(self):
        return self.data

if __name__ == "__main__":
    source = "data/cleaned_data.csv"
    loader = CSVLoader(source)
    data = loader.load(source)
    prepper = DataPrep(data)
    prepper.label_encode_cols()
    print(prepper.get_data())
