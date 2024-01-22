#!/usr/bin/env python
# coding: utf-8

# In[3]:


#pip install ipython
#pip install --upgrade nbformat

# Importando pacotes para processamento de dados
import pandas as pd  # Pacote para manipulação de dados em formato tabular
import csv  # Pacote para leitura e escrita de arquivos CSV

import numpy as np

# Importando bibliotecas para trabalhar com arquivos e diretórios
import os  # Biblioteca para interação com o sistema operacional

#importando bibliotecas para trabalhar com graficos
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
from plotly.subplots import make_subplots


# In[4]:
'''

# Obtém o caminho do diretório atual
diretorio_atual = os.getcwd()
# Caminho para a pasta contendo os arquivos CSV
pasta_csv = os.path.join(diretorio_atual, 'DATA')
print(pasta_csv)


# In[5]:


# Lista dos anos de 2002 a 2022
anos = list(range(2001, 2023))

# Lista para armazenar os DataFrames de cada arquivo CSV
lista_dataframes = []

for ano in anos:
    # Nome do arquivo CSV para o ano atual
    nome_arquivo = f'DATA_{ano}.CSV'
    
    # Caminho completo para o arquivo CSV
    caminho_arquivo = os.path.join(pasta_csv, nome_arquivo)
    
    # Verifica se o arquivo existe antes de realizar as operações
    if os.path.exists(caminho_arquivo):
        # Lê o CSV e adiciona à lista
        df_temp_brasilia = pd.read_csv(caminho_arquivo, header=0, sep=';')
        lista_dataframes.append(df_temp_brasilia)

        print(f'Leitura concluída para {nome_arquivo}. DataFrame criado para o ano {ano}')
    else:
        print(f'O arquivo {nome_arquivo} não foi encontrado.')


#mudando o tipo da coluna Data para datetime
for idx in range(len(lista_dataframes)):
    lista_dataframes[idx]['Data'] = pd.to_datetime(lista_dataframes[idx]['Data'])

# Exemplo de acesso ao DataFrame para o ano de 2002
# df_2002 = lista_dataframes[0]


# In[6]:

lista_dataframes[0]


# In[7]:


lista_dataframes[0].info()


# In[8]:


lista_dataframes[0]['Temperatura Maxima'].unique()

'''
# In[49]:


def criar_grafico_media_diaria(caminhoPasta, ano, coluna):
    df = pd.read_csv(f'{caminhoPasta}/Data/DATA_{ano}.CSV', sep=';')
    # Tenta ler o arquivo .csv
    df['Data'] = pd.to_datetime(df['Data'])

    # Selecione o intervalo de datas do seu DataFrame
    data_inicio = df['Data'].min()
    data_fim = df['Data'].max()

    # Crie um intervalo de datas diárias
    intervalo_datas = pd.date_range(start=data_inicio, end=data_fim, freq='MS')

    # Calcular a média da temperatura para cada dia
    media_por_dia = df.groupby(df['Data'].dt.to_period('D'))[coluna].mean().reset_index().round(1)

    # Converter Period para str
    media_por_dia['Data'] = media_por_dia['Data'].dt.strftime('%Y-%m-%d')

    # Crie uma figura vazia
    fig = go.Figure()
    fig.update_layout(width=1400, height=1000)

    # Adicionar trace de linha para a média por dia
    fig.add_trace(go.Scatter(x=media_por_dia['Data'], y=media_por_dia[coluna],
                             mode='lines+markers', 
                             name='Média por Dia',
                             marker=dict(color='blue', size=8),
                             hoverinfo='text+x+y',
                             text='Média: ' + media_por_dia[coluna].astype(str) + '°C',
                             visible=True  # Inicialmente visível
                             ))

    # Ajustar a ordem dos rótulos do eixo x
    fig.update_xaxes(tickvals=intervalo_datas, ticktext=intervalo_datas.strftime('%Y-%m'))
    
    # Adicionar título e rótulos dos eixos
    fig.update_layout(
        font_family='Arial',
        font_color='black',
        font_size=24,
        title=f'Média Diária de {coluna}',
        xaxis_title='Data',
        yaxis_title=f'{coluna}',
    )

    # Salvar o gráfico em um arquivo HTML
    #pio.write_html(fig, file=namearq, include_plotlyjs='cdn', full_html=False)

    # Salvar a figura como um arquivo PNG em uma pasta específica
    fig.write_image(os.path.join(f'{caminhoPasta}/assets/img.png'), format='png', width=1400, height=1000)


    # Exibir o gráfico interativo
    #pio.show(fig)


# In[50]:
'''

criar_grafico_media_diaria(lista_dataframes, 'teste')

'''
# In[ ]:


#funcação para Imprimir os graficos
#for idx, dataframe in enumerate(lista_dataframes):
 #   year = idx + 2001
  #  criar_grafico_media_diaria(dataframe, f'temperatura_{year}')
    

