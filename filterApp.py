import pandas as pd
import matplotlib.pyplot as plt
import funcoes as func

def filtrar(caminhoPasta, ano, coluna):
    base = caminhoPasta + 'DATA_' + ano + '.CSV'
    # Caminho do arquivo .csv

    df = pd.read_csv(base, sep=';')

    # func.meanDf(df, ano, coluna)
