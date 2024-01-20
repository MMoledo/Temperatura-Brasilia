import PySimpleGUI as sg
# Lib pra fazer o menu visível
from PIL import Image, ImageTk 
#Image para criar um objeto de imagem, ImageTk para exibir
import filterApp
# Função que aplica a filtragem
import os
# Lib para manipulação de arquivos

theme = sg.theme('DarkBrown7')
# Tema de cores e exibição dos menus

caminhoPasta = ''
# Inicia uma variavel para armazenar o caminho da pasta selecionada
# A importância dela começar vazia se deve à verificação da existência de arquivos .csv na pasta

menu_layout = [['Arquivo', ['Abrir', 'Sair']]]
# Menu de opções superior

def file_layout():
    layout = [[sg.Text('Pasta'), sg.In(size=(25,1), enable_events=True ,key='-FOLDER-'), sg.FolderBrowse(button_text='Selecionar')]]
    return sg.Window('Seleção de Pastas', layout)
'''
file_layout = [
    [sg.Text('Pasta'), sg.In(size=(25,1), enable_events=True ,key='-FOLDER-'), sg.FolderBrowse(button_text='Selecionar')]
]
'''
# Layout da seleção de pasta

layout = [[sg.Menu(menu_layout)],
          [sg.Text('Selecione o seu filtro:'),
           sg.Combo(['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'], default_value='2020', key='-ANO-'),
           sg.Combo(['Temperatura Exata', 'Temperatura Máxima', 'Temperatura Mínima', 'Umidade do Ar', 'Velocidade do Vento'], key='-COLUNA-', default_value='Temperatura Exata')],
           [sg.Button('Filtrar', size=(10, 1))],
           [sg.Image(key='-IMAGE-', visible=False)]
]
# Layout da janela principal
        
window = sg.Window('Análise de Temperatura', layout, resizable=True)
# Criação da janela principal

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    # Encerra a exibição da janela principal

    elif event == 'Abrir':
        #file_window = sg.Window('Selecionar Pasta', file_layout)
        file_window = file_layout()
        while True:
            file_event, file_values = file_window.read()
            if file_event == sg.WINDOW_CLOSED:
                break
            # Encerra a exibição da janela de seleção de pasta

            elif file_event == '-FOLDER-':
                caminhoPasta = file_values['-FOLDER-']
                if os.path.isdir(caminhoPasta):
                # Verifica se o caminho é válido
                    arquivos = [arquivo for arquivo in os.listdir(caminhoPasta) if (arquivo.endswith('.csv') or arquivo.endswith('.CSV'))]
                    # Lista os arquivos .csv da pasta selecionada
                    if arquivos:
                    # Verifica se os arquivos são válidos
                        file_window.close()
                        file_window = None
                    else:
                        sg.popup_error('Nenhum arquivo .csv encontrado na pasta selecionada.')
                else:
                    sg.popup_error('Caminho de pasta inválido.')
            break
    # Exibe a janela de seleção de pasta
            
    elif event == 'Filtrar':
        if caminhoPasta == '':
            sg.popup_error('Selecione uma pasta válida.') 
            continue 

        ###filterApp.filtrar(caminhoPasta, values['-ANO-'], values['-COLUNA-'])
        # Chama a função de filtragem

        image = Image.open("assets/img.png")
        # Cria o objeto de imagem
        window['-IMAGE-'].update(
            data = ImageTk.PhotoImage(image)
        )
        # Atribui o objeto ao elemento da janela

        window['-IMAGE-'].update(visible=True)
        # Altera o critério de visibilidade da imagem
    # Exibe a imagem respectiva ao filtro selecionado

window.close()
