import os

# Base project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths for raw data (Excel files)
RAW_DATA_PATH = os.path.join(BASE_DIR, "../data/raw/")



# Predictions Table Name
PREDICTIONS_TABLE = "predictions"

# model evaluation
EVALUATION_TABLE = "grid_search_results"

# Logging Configuration
LOGGING_LEVEL = "INFO"

#saved models
#MODELS_PATH ="../models/"      #funziona se lancio da notebook ma non con streamlit

MODELS_PATH = os.path.abspath(os.path.join(BASE_DIR, "../models/"))  # 👈 PATH ASSOLUTO
