# house-price-prediction-pipeline
Predict House Price Web Application

Struttura progetto:

progetto/
│
├── data/
│   └── raw/
│       └── Real estate valuation data set.xlsx
│
├── models/
│   └── coordinates_model.pickle
│   └── conditions_model.pickle
│
├── src/
│   ├── config.py
│   ├── preprocess.py
│   ├── make_model.py
│
├── scripts/
│   ├── UI.py
│   └── run_pipeline.py
 

Descrizione del Modello e del Dataset

Modello:
Questa applicazione web utilizza un modello di Random Forest per prevedere il prezzo di una casa. Il modello è stato addestrato sui dati del dataset utilizzando due diverse modalità di previsione:

-Previsione basata sulle coordinate geografiche: L'utente fornisce la latitudine e longitudine della casa, e il modello prevede il prezzo in base alla posizione geografica.

-Previsione basata sulle condizioni dell'appartamento: L'utente fornisce l'età dell'appartamento, la distanza dalla stazione e il numero di negozi nei dintorni, e il modello fornisce una previsione del prezzo.


Dataset:
Il dataset utilizzato per addestrare il modello contiene informazioni sugli immobili della regione di Sindian, Nuova Taipei, Taiwanu, tra cui incluse:

*Latitudine e Longitudine: Coordinate geografiche dell'appartamento.

*Età della casa: Anni dalla costruzione.

*Distanza dalla stazione: Distanza dall'appartamento alla stazione di metro più vicina.

*Numero di negozi: Numero di negozi nei dintorni.

*Prezzo per unità di superficie: sarà la nostra variabile target, ossia il prezzo medio dell'immobile per metro quadrato.


Prima di eseguire l'applicazione, assicurati di aver addestrato i modelli di regressione utilizzando run_pipeline.py. 
Questo script allenerà il modello sui dati e salverà i modelli addestrati nella cartella models.

Avviare l'Applicazione Streamlit:
Una volta che i modelli sono addestrati, puoi avviare l'applicazione Streamlit. Esegui il seguente comando:
streamlit run scripts/UI.py

L'applicazione si aprirà nel browser, mostrando l'interfaccia per selezionare il tipo di ricerca (coordinate geografiche o condizioni dell'appartamento), e permetterà di inserire i dati per la previsione del prezzo.

