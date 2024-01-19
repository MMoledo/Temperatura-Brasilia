import PySimpleGUI as sg
from PIL import Image, ImageTk #Image for open, ImageTk for display


theme = sg.theme('DarkBrown7')

# Define the menu layout
menu_layout = [['Arquivo', ['Abrir', 'Sair']]]

file_layout = [
    [sg.Text('Pasta'), sg.In(size=(25,1), enable_events=True ,key='-FOLDER-'), sg.FolderBrowse(button_text='Selecionar')]
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
           [sg.Button('Filtrar', size=(10, 1))],
           [sg.Image(key='-IMAGE-', visible=False)]
        ]  # Add this line to display the image
        # Create the window
        
window = sg.Window('Análise de Temperatura', layout, resizable=True)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
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
    elif event == 'Filtrar':
        print('Filtrando...')

        image = Image.open("assets/img.png") #I prefer /
        window['-IMAGE-'].update(
            data = ImageTk.PhotoImage(image)
        ) #update the myimg key

        window['-IMAGE-'].update(visible=True) # Show the image

window.close()
