
import os
import sys
sys.path.append(os.path.abspath('..')) 
from src import config
from src.preprocess import preprocess_data

import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor  # Importa RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import GradientBoostingRegressor



# Carica i dati preprocessati
def load_data():
    # Esegui il preprocessing dei dati
    X, y = preprocess_data()  # Supponendo che preprocess_data restituisca X, y
    return X, y

# Funzione per addestrare il modello
def train_model(input_type="coordinates"):
    # Funzione per addestrare i modelli per "coordinates" o "conditions"
    if input_type == "coordinates":
        # Carica i dati e allena il modello per coordinate
        X, y = preprocess_data(input_type="coordinates")
    elif input_type == "conditions":
        # Carica i dati e allena il modello per condizioni appartamento
        X, y = preprocess_data(input_type="conditions")

    # Suddividi i dati in train e test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=200, max_features='sqrt', random_state=42)
    model.fit(X_train, y_train)

    # Salvataggio modello
    model_path = os.path.join(config.MODELS_PATH, f'{input_type}_model.pickle')
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

    print(f"Modello {input_type} salvato.")
