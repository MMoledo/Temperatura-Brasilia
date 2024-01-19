import os 
import pandas as pd
import numpy as np

for arquivo in os.listdir("Data"):
    df = pd.read_csv("Data/" + arquivo)
    df.drop(columns=["Pressao","Pressao2","Pressao3","Temperatura Ponto de Orvalho","X","Y","Z","W","Vento","Vento Rajada Maxima"], inplace=True)
    df['Data'] = pd.to_datetime(df['Data'])
    df['Temperatura'] = df['Temperatura'].str.replace(',','.').astype(float)
    condition = (df['Temperatura'] < -10)
    df_filtered = df.drop(df[condition].index)
    
    # Salvando as alteracoes
    df_filtered.to_csv("Data/" + arquivo, index=False)