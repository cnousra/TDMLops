from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import joblib

app = FastAPI()

# Charger le modèle avec les noms des classes
model = joblib.load('model.pkl')

class Item(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict(item: Item):
    try:
        features = [[item.sepal_length, item.sepal_width, item.petal_length, item.petal_width]]
        prediction = model['model'].predict(features)
        class_names = model['class_names']
        predicted_class_name = class_names[prediction[0]]  # Obtenir le nom de la classe prédite
        return {"predicted_class": predicted_class_name}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Erreur de prédiction: {}".format(e))
