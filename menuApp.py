import PySimpleGUI as sg
# Lib pra fazer o menu visível
from PIL import Image, ImageTk 
#Image para criar um objeto de imagem, ImageTk para exibir
import filtroApp
# Função que aplica a filtragem
import os
# Lib para manipulação de arquivos
import time
from grafico import criar_grafico_media_diaria

theme = sg.theme('LightBrown6')
# Tema de cores e exibição dos menus

caminhoPasta = ''
# Inicia uma variavel para armazenar o caminho da pasta selecionada
# A importância dela começar vazia se deve à verificação da existência de arquivos .csv na pasta

menu_layout = [['Arquivo', ['Abrir', 'Sair']]]
# Menu de opções superior

layout = [[sg.Menu(menu_layout)],
          [sg.Text('Selecione o seu filtro:'),
           sg.Combo(['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'], default_value='2020', key='-ANO-', readonly=True),
           sg.Combo(['Temperatura', 'Temperatura Minima', 'Temperatura Maxima', 'Umidade do Ar', 'Velocidade do Vento', 'Precipitacao', 'Radiacao'], default_value='Temperatura', key='-COLUNA-', readonly=True),
           sg.Button('Filtrar', size=(10, 1)),
           sg.ProgressBar(100, orientation='h', expand_x=True, size=(20, 20), visible=False, key='-PROGRESS-')],
           [sg.Image(key='-IMAGE-', visible=False, expand_x=True, expand_y=True, size=(100,100))],
]
# Layout da janela principal
        
window = sg.Window('Análise de Temperatura', layout)
# Criação da janela principal

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    # Encerra a exibição da janela principal

    elif event == 'Abrir':
        caminhoPasta = ''
        while not os.path.isdir(caminhoPasta):
            caminhoPasta = sg.popup_get_folder('Selecione a pasta com os arquivos', default_path=os.getcwd())
            
    elif event == 'Filtrar':
        if caminhoPasta == '':
            sg.popup_error('Selecione uma pasta válida.') 
            continue 
        # Verifica se o caminho da pasta foi selecionado

        window['-PROGRESS-'].update(visible=True)
        # Altera o critério de visibilidade da barra de progresso

        for x in range(100):
            time.sleep(0.001)
            window['-PROGRESS-'].update_bar(x + 1)
        # Simula o progresso da filtragem
            
        coluna = values['-COLUNA-']    
        match values['-COLUNA-']:
            case 'Velocidade do Vento':
                coluna = 'Vento Velocidade'
            case 'Precipitacao':
                coluna = ' Precipitacao'

        try:
            criar_grafico_media_diaria(caminhoPasta, values['-ANO-'], coluna)
            image = Image.open("assets/img.png")
            # Cria o objeto de imagem
        except:
            req = filtroApp.filtrar(f'{caminhoPasta}/Data/', values['-ANO-'], coluna)
            # Chama a função de filtragem
            
            if req == 0:
                sg.popup_error('Erro ao filtrar.')
                continue
            # Verifica se ocorreu algum erro na filtragem

            image = Image.open("assets/img.png")
            # Cria o objeto de imagem
        finally:
            image = image.resize((1120,580),Image.ANTIALIAS)
            window['-IMAGE-'].update(
                data = ImageTk.PhotoImage(image)
            )
            # Atribui o objeto ao elemento da janela

            window['-IMAGE-'].update(visible=True)
            # Altera o critério de visibilidade da imagem
    # Exibe a imagem respectiva ao filtro selecionado

window.close()

