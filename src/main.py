from fastapi import FastAPI
from pathlib import Path
import pandas as pd
from pydantic import BaseModel
from contextlib import asynccontextmanager
import pickle

MODELPATH = Path("../rf.sav")
MODELVERSION = "0.0.9"

# expected request input for prediction
class InputData(BaseModel):
    total_charges: float 
    monthly_charges: float
    payment_method: float

models = {}

# load model before accepting requests
@asynccontextmanager
async def lifespan(app: FastAPI):
    # load model 
    models["rf"] = pickle.load(open(MODELPATH, "rb"))

    yield
    # write potential cleanup here

app = FastAPI(lifespan = lifespan)

@app.get("/")
def index():
    return "Hello world"

@app.post("/predict")
def predict(input: InputData):
    
    input_dict = input.model_dump()

    X = pd.DataFrame(data = {
        "total_charges": [input_dict["total_charges"]],
        "monthly_charges": [input_dict["monthly_charges"]],
        "payment_method": [input_dict["payment_method"]]
    })

    res = {
        "prediction": float(models["rf"].predict(X)),
        "model": MODELVERSION
    }

    return res

