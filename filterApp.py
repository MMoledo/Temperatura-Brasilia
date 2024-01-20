import pandas as pd
import matplotlib.pyplot as plt


def filtrar(caminhoPasta, ano, coluna):
    base = caminhoPasta + 'DATA_' + ano + '.csv'
    # Caminho do arquivo .csv

'''
    %run Functions.ipynb
    # Carregar as funções de organização dos dataframes
    
    match coluna:
        case 'Temperatura':
            df = tempExat(base)
        case 'Temperatura Maxima':
            df = tempMax(base)
        case 'Temperatura Minima':
            df = tempMin(base)
        case 'Umidade do Ar':
            df = umidadeAr(base)
        case 'Vento Velocidade':
            df = velVento(base)

    plt.plot(df['Data'], df[f'{coluna}'])
    plt.xlabel('Data')
    plt.ylabel(f'{coluna}')
    plt.title('Variação de ' + coluna + ' em ' + ano)
    plt.grid(True)
    # Criação do gráfico

    plt.savefig('assets/img.png')
    # Salva a imagem gerada
    '''
