from fastapi import FastAPI
import uvicorn
import pickle
from model import Woman

app = FastAPI()

# reading the pickle file where we store our model
model = pickle.load(open("model.pkl","rb"))

@app.get("/")
def greet():
    return {'Hello World from python'}

# posting data so that model can predict
@app.post("/predict")
def predict(req:Woman):
    preg=req.pregnancies
    glucose=req.glucose
    bp=req.bp
    skinthickness=req.skinthickness
    insulin=req.insulin
    bmi=req.bmi
    dpf=req.dpf
    age=req.age
    features = list([preg,glucose,bp,skinthickness,insulin,bmi,dpf,age])
    # predicting 
    pred = model.predict([features])
    # return {"Ans {}".format(pred)}

    probab = model.predict_proba([features])

    if(pred == 1):
        return {"ans": "You have been tested positive with {} probability".format(probab[0][1])}
    else:    
        return {"ans": "You have been tested negative with {} probability".format(probab[0][0])}
        


# command for run the app "uvicorn app:app --reload"
if __name__ == '__main__' :
    uvicorn.run(app)