import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file = '/Users/edoardoiannelli/desktop/progetto/data/raw/Real estate valuation data set.xlsx'


df = pd.read_excel(file  ) 
print(df.head())

print(df.dtypes)


print(df.shape)             # Righe e colonne
'''
print(df.columns)           # Nomi colonne
print(df.dtypes)            # Tipi di dato
print(df.head())            # Prime 5 righe
print(df.describe())        # Statistiche numeriche


#Valori mancanti e duplicati
print(df.isnull().sum())         # Conta i NaN
print(df.duplicated().sum())     # Conta i duplicati


#Distribuzione delle variabili
## Variabili numeriche
df.hist(bins=30, figsize=(15,10))
plt.show()

# Variabili categoriche
print(df['categoria'].value_counts())
sns.countplot(x='categoria', data=df)
plt.show()


#Correlazioni tra variabili numeriche
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Matrice di correlazione")
plt.show()

#Outlier detection (es. con boxplot)
sns.boxplot(x=df['variabile'])
plt.show()

# Relazioni tra variabili (scatter, pairplot)
sns.pairplot(df, hue='target')  # Se hai una variabile target
plt.show()

SCHEMA

1. Config.py
Definisci i path (dati, modelli, ecc.)

2. load_data.py
Carica i dati dal .csv o .xlsx con i campi X1-X6, Y

3. preprocess.py
Normalizza, rimuovi outlier, converte tipi, split X/Y

4. make_model.py
Addestra il modello (es. LinearRegression, RandomForestRegressor)

Salva il modello .pickle

5. run_pipeline.py
Esegue tutti i passaggi in ordine

6. ui.py
Interfaccia Streamlit con input: Latitudine e Longitudine

Predice e mostra il prezzo