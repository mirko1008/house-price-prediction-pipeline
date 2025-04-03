import pandas as pd
import sys
import os
from scipy.stats import zscore
sys.path.append(os.path.abspath('..')) 
from src import config
dataset_path = os.path.join(config.RAW_DATA_PATH, "Real estate valuation data set.xlsx")

def get_min_max():
    # Carica il dataset
    df = pd.read_excel(dataset_path)
    
    # Calcola i limiti minimi e massimi per le variabili di interesse
    lat_min, lat_max = df['X5 latitude'].min(), df['X5 latitude'].max()
    long_min, long_max = df['X6 longitude'].min(), df['X6 longitude'].max()
    age_min, age_max = df['X2 house age'].min(), df['X2 house age'].max()
    distance_min, distance_max = df['X3 distance to the nearest MRT station'].min(), df['X3 distance to the nearest MRT station'].max()
    stores_min, stores_max = df['X4 number of convenience stores'].min(), df['X4 number of convenience stores'].max()
    
    # Restituisci un dizionario con i limiti
    return {
        'latitude': (lat_min, lat_max),
        'longitude': (long_min, long_max),
        'age': (age_min, age_max),
        'distance': (distance_min, distance_max),
        'stores': (stores_min, stores_max)
    }

# Chiamalo per ottenere i limiti minimi e massimi
min_max_values = get_min_max()


def preprocess_data(input_type="coordinates"):
    # Carica il dataset
    df = pd.read_excel(dataset_path)

    # Preprocessing
    #df = df.dropna()  # Rimozione dei valori mancanti -> non ci sono valori mancanti

    # Separazione tra variabili indipendenti (X) e dipendenti (Y)
    if input_type == "coordinates":
        X = df[['X5 latitude', 'X6 longitude']]  # Coordinate geografiche
    elif input_type == "conditions":
        X = df[['X2 house age', 'X3 distance to the nearest MRT station', 'X4 number of convenience stores']]  # Condizioni appartamento

    y = df['Y house price of unit area']  # Prezzo della casa

    return X, y
