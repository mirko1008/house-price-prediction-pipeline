
#run_pipeline
import os, sys

#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#sys.path.append(os.path.abspath('..'))  # Aggiungi la cartella principale del progetto al sys.path
import logging
sys.path.append(os.path.abspath('..'))
from src import config
from src.preprocess import preprocess_data
from src.make_model import train_model


# Set up logging
logging.basicConfig(filename='../log/pipeline.log', level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("Inizio della pipeline di machine learning")

    # Fase 1: Preprocessing dei dati
    logging.info("Fase 1: Preprocessing dei dati")
    X, y = preprocess_data()  # Chiama la funzione di preprocessing per ottenere X e y
    logging.info(f"Fase 1 completata: Dati preprocessati (X: {X.shape}, y: {y.shape})")

    # Fase 2: Addestramento del modello per le coordinate
    logging.info("Fase 2: Addestramento del modello per coordinate")
    train_model(input_type="coordinates")

    # Fase 3: Addestramento del modello per le condizioni
    logging.info("Fase 3: Addestramento del modello per condizioni")
    train_model(input_type="conditions")

    logging.info("Pipeline completata con successo!")

# Avvia la pipeline
if __name__ == "__main__":
    main()
