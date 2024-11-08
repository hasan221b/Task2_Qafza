#This app is to predict diamon price based on diamond features 
# yo can test it using test.py file 

from fastapi import FastAPI
import pickle
from pydantic import BaseModel

app = FastAPI()

#model that prdict diamond price
with open('rfmodel.pkl', 'rb') as file:
    model = pickle.load(file)

#class contains diamond featres
class Diamond(BaseModel):
    cart: float
    x: float
    y: float
    z: float

@app.get("/")
def read_root():
    return {"message": "Starting... "}

@app.post("/price/")
def add_numbers(nu: Diamond):
    new_data = [[nu.cart,nu.x,nu.y,nu.z]]  
    predictions = model.predict(new_data)
    print(predictions)
    return {"Diamond price  is: ", predictions[0]}