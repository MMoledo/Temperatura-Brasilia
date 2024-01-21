import pandas as pd
import matplotlib.pyplot as plt
import funcoes as func

def filtrar(caminhoPasta, ano, coluna):
    base = caminhoPasta + '/' if caminhoPasta[-1] != '/' else caminhoPasta
    base += 'DATA_' + ano + '.CSV'
    # Caminho do arquivo .csv

    df = pd.read_csv(base, sep=';')

    df = func.meanDf(df, ano, coluna)
    # Cria o dataframe com a média dos valores

    if df is not None and func.mkImg(df, ano, coluna) != 0:
        plt.close()
        plt.clf()
        plt.cla()
        # Limpa a memória da imagem

        return 1
    else:
        return 0
        # Retorna 0 caso ocorra algum erro