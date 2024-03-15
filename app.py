import uvicorn
import pandas as pd 
from pydantic import BaseModel
from typing import Literal, List, Union
from fastapi import FastAPI, File, UploadFile
import joblib


description = """

## Bienvenue sur l'estimateur de prix Getaround !  

Cette API donne une estimation du prix de location journalier de votre voiture grâce à un modèle de machine learning.  

Pour ce faire, veuillez suivre les indications ci-dessous.  

### 🔌 L'API possède deux endpoints :

1. `/`: **GET** le chemin par défaut ;

2. `/predict` : **POST** le chemin pour obtenir vos prédictions. 

Afin d'obtenir les prédictions, vous devrez renseigner les éléments suivants : 

* **Marque** : la marque de la voiture (chaîne de caractères)
* **Kilométrage** : en km (nombre entier)
* **Puissance** du moteur** : en chevaux (nombre entier)
* **Carburant** : essence, diesel, électrique ou hybride (chaîne de caractères)
* **Couleur** : la couleur de la voiture (chaîne de caractères)
* **Type de véhicule** : citadine, coupée, SUV, familiale, etc. (chaîne de caractères)
* **Parking privé** : oui/non (nombre entier : 1 pour oui et 0 pour non)
* **GPS** : oui/non
* **Climatisation** : oui/non
* **À boîte automatique** : oui/non
* **Getaround Connect** : oui/non
* **Régulateur de vitesse** : oui/non
* **Pneus d'hiver** : oui/non

Ces informations doivent être renseignées sous la forme d'une liste de 13 éléments. 

### 🚗 Exemple :

Voici un exemple pour une voiture Peugeot rouge compacte essence avec 20000 km au compteur :
* sans parking privé
* sans GPS
* avec climatisation
* à boîte manuelle
* avec Getaround Connect
* sans régulateur de vitesse
* sans pneus d'hiver

Input à renseigner : 

{
  "InputList": **["Peugeot", 20000, 48, "petrol", "red", "subcompact", 0, 0, 1, 0, 1, 0, 0]**
}

Nous obtenons une prédiction de : 110,39 euros/jour.

#### À vous de jouer ! ✨🔮✨

"""

tags_metadata = [
    {
        "name": "Introduction",
        "description": "Page d'entrée par défaut",
    },
    {
        "name": "Prédiction machine learning",
        "description": "Estimation du prix de location"
    }
]

# FastAPI instance
app = FastAPI(
    title = 'Estimateur de prix Getaround',
    description=description,
    openapi_tags=tags_metadata
)

# Predict function
class PredictionPrice(BaseModel):
    InputList: list

# Get method
@app.get("/", tags=["Introduction"])
async def index():
    message = "Bienvenue ! Vous êtes sur l'estimateur de prix Getaround. Merci de vous rendre à l'adresse /docs pour pouvoir utiliser cette API."
    return message

# Post method
@app.post("/predict", tags=["Prédiction machine learning"])
async def predict(data: PredictionPrice):

    # Import data
    pricing = pd.read_csv('price_predictor/src/get_around_pricing_project.csv')
    preprocessor = joblib.load('price_predictor/src/preprocessor.pkl')
    loaded_model = joblib.load('price_predictor/src/model.pkl')

    # Input 
    input_data = pd.DataFrame([data.InputList], columns=pricing.iloc[:,:-1].columns)
    input_data = preprocessor.transform(input_data)

    # Make predictions
    prediction = loaded_model.predict(input_data)

    # Format response
    response = {"prediction": prediction.tolist()[0]}
    return response

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000)