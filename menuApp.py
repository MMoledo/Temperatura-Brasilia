import PySimpleGUI as sg

theme = sg.theme('DarkBrown7')

# Define the menu layout
menu_layout = [['File', ['Open', 'Exit']]]

file_layout = [
    [sg.Text('Folder'), sg.In(size=(25,1), enable_events=True ,key='-FOLDER-'), sg.FolderBrowse()]
]

# Create the window layout
layout = [[sg.Menu(menu_layout)],
          [sg.Text('Selecione o seu filtro:')],
          [sg.Radio('Anos 60', "filtro", default=True), 
           sg.Radio('Anos 70', "filtro", default=False), 
           sg.Radio('Anos 80', "filtro", default=False), 
           sg.Radio('Anos 90', "filtro", default=False), 
           sg.Radio('Anos 2000', "filtro", default=False), 
           sg.Radio('Anos 2010', "filtro", default=False),
           sg.Radio('Anos 2020', "filtro", default=False)],
           [sg.Button('Filtrar', size=(10, 1))]
]

# Create the window
window = sg.Window('Análise de Temperatura', layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Open':
        file_window = sg.Window('Selecionar Pasta', file_layout)
        while True:
            file_event, file_values = file_window.read()
            if file_event == sg.WINDOW_CLOSED or file_event == 'Exit':
                break
            elif file_event == '-FOLDER-':
                folder = file_values['-FOLDER-']
                print(folder)
                file_window.close()
                break
window.close()
