#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas
import os
import matplotlib.pyplot as plt
# Imports das libs para o modelo


# In[27]:


def listLines():
    for arquivo in os.listdir('.\\Data\\'):
        if arquivo.endswith('.CSV'):
            df = pandas.read_csv('Data/' + arquivo, sep=';')
            print('=' * 50)
            print(arquivo)
            print('\n')
            print(df.head(5))
            print('\n')
            print(df.dtypes)
            print('\n')


# In[28]:


def meanDf(df, ano, coluna):
    if not df.empty:
        df = df.groupby(['Data'])[coluna].mean().round(1)
        df = df.reset_index()
        return df


# In[29]:


def medianDf(df, ano, coluna):
    if not df.empty:
        df = df.groupby(['Data'])[coluna].median().round(1)
        df = df.reset_index()
        return df


# In[30]:


def mkImg(df, ano, coluna):
    if not df.empty:
        plt.figure(figsize=(15, 5))
        plt.plot(df['Data'], df[coluna])
        plt.title('Média de ' + coluna + ' em ' + ano)
        plt.xlabel('Data')
        plt.ylabel(coluna)
        try:
            plt.savefig('assets/img.png')
        except:
            return 0
        else:
            plt.close()
            plt.clf()
            plt.cla()
            # Limpa a memória da imagem
            return 1


# In[32]:


# Ambiente de teste >>>>>>>>>
'''
df = pandas.read_csv('Data/DATA_2001.CSV', sep=';')
df = meanDf(df, '2001', 'Temperatura')
print(df)
print(mkImg(df, '2001', 'Temperatura'))
'''

