import PySimpleGUI as sg
from PIL import Image, ImageTk #Image for open, ImageTk for display


theme = sg.theme('DarkBrown7')
# Tema de cores e exibição dos menus


menu_layout = [['Arquivo', ['Abrir', 'Sair']]]
# Menu de opções superior

file_layout = [
    [sg.Text('Pasta'), sg.In(size=(25,1), enable_events=True ,key='-FOLDER-'), sg.FolderBrowse(button_text='Selecionar')]
]
# Layout da seleção de pasta

layout = [[sg.Menu(menu_layout)],
          [sg.Text('Selecione o seu filtro:'),
           sg.Combo(['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'], default_value='2020', key='-ANO-'),
           sg.Combo(['Temperatura', 'Umidade', 'Pressão', 'Velocidade do Vento'], key='-COLUNA-')],
          [sg.Radio('Anos 60', "filtro", default=True), 
           sg.Radio('Anos 70', "filtro", default=False), 
           sg.Radio('Anos 80', "filtro", default=False), 
           sg.Radio('Anos 90', "filtro", default=False), 
           sg.Radio('Anos 2000', "filtro", default=False), 
           sg.Radio('Anos 2010', "filtro", default=False),
           sg.Radio('Anos 2020', "filtro", default=False)],
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
        file_window = sg.Window('Selecionar Pasta', file_layout)
        while True:
            file_event, file_values = file_window.read()
            if file_event == sg.WINDOW_CLOSED or file_event == 'Sair':
                break
            elif file_event == '-FOLDER-':
                folder = file_values['-FOLDER-']
                print(folder)
                file_window.close()
                break
    # Exibe a janela de seleção de pasta
            
    elif event == 'Filtrar':
        print('Filtrando...')

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
