import os
import sys

# Aggiunge la root del progetto (progetto/) al path per importare `src`
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

import streamlit as st
import pickle
import numpy as np
from src import config
from src.preprocess import get_min_max

# Carica i limiti minimi e massimi
min_max_values = get_min_max()

# Chiedi all'utente di scegliere quale modello usare
option = st.radio("Seleziona l'opzione di ricerca:",
                  ('Ricerca per coordinate geografiche', 'Ricerca per condizioni appartamento'))

# Carica il modello scelto
if option == 'Ricerca per coordinate geografiche':
    with open(os.path.join(config.MODELS_PATH, 'coordinates_model.pickle'), 'rb') as f:
        model = pickle.load(f)

elif option == 'Ricerca per condizioni appartamento':
    with open(os.path.join(config.MODELS_PATH, 'conditions_model.pickle'), 'rb') as f:
        model = pickle.load(f)

# Input dell'utente
if option == 'Ricerca per coordinate geografiche':
    latitude = st.number_input("Latitudine", value=25.0, min_value=min_max_values['latitude'][0], max_value=min_max_values['latitude'][1])
    
    # Verifica se il valore di longitudine è minore del minimo, altrimenti usa il valore minimo
    longitude_default = max(121.0, min_max_values['longitude'][0])  # Assicurati che il valore iniziale non sia sotto il minimo
    longitude = st.number_input("Longitudine", value=longitude_default, min_value=min_max_values['longitude'][0], max_value=min_max_values['longitude'][1])
    
    input_data = np.array([[latitude, longitude]])  # Crea array 2D per il modello

elif option == 'Ricerca per condizioni appartamento':
    # Modifica qui per assicurarti che i valori siano float
    age = st.number_input("Età dell'appartamento", value=float(10), min_value=float(min_max_values['age'][0]), max_value=float(min_max_values['age'][1]))
    
    # Verifica che il valore predefinito della distanza non sia inferiore al minimo
    distance_default = max(2.0, min_max_values['distance'][0])  # Imposta il valore predefinito al minimo se inferiore
    distance = st.number_input("Distanza dalla stazione", value=distance_default, min_value=float(min_max_values['distance'][0]), max_value=float(min_max_values['distance'][1]))
    
    # Verifica che il valore predefinito del numero di negozi sia sopra il minimo
    stores_default = max(5, min_max_values['stores'][0])  # Imposta il valore predefinito al minimo se inferiore
    stores = st.number_input("Numero di negozi", value=float(stores_default), min_value=float(min_max_values['stores'][0]), max_value=float(min_max_values['stores'][1]))
    
    input_data = np.array([[age, distance, stores]])

# Predizione quando clicchi il bottone
if st.button("Prevedi Prezzo"):
    input_scaled = input_data  # Se hai bisogno di scaler, applicalo qui
    predicted_price = model.predict(input_scaled)[0]
    st.write(f"Il prezzo previsto della casa è: {predicted_price:.2f}")
