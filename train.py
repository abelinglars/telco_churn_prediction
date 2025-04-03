# Train the data
from sklearn.model_selection import train_test_split
from sklearn.base import BaseEstimator
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

from data_prep import DataPrep
from data_cleaning import CSVLoader

class Trainer():
    def __init__(self, data):
        self.data = data
        self.model = BaseEstimator

    def split_data(self, params):
        return train_test_split(**params)

    def show(self):
        print(self.data)

    def train(self, 
              X_cols: list[str],
              target: list[str],
              model,
              split_params,
              model_params):

        X = self.data[X_cols]
        y = self.data[target]

        (
            X_train, 
            X_test, 
            y_train,
            y_test
        ) = train_test_split(X, y,
                             **split_params)
	
        self.model = model(**model_params)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        print(accuracy_score(y_test, y_pred))

if __name__ == "__main__":

    # load data
    source = "data/cleaned_data.csv"
    loader = CSVLoader(source)
    prep = DataPrep(loader.load(source))
    prep.label_encode_cols()
    trainer = Trainer(prep.get_data())
    trainer.show()

    model_params = {
        "n_estimators": 50
    }

    split_params = {
        "test_size": 0.2
    }

    trainer.train(
        X_cols = ["total_charges", "monthly_charges", "payment_method"],
        model = RandomForestClassifier,
        target = "churn",
        split_params = split_params,
        model_params = model_params
    )
    
