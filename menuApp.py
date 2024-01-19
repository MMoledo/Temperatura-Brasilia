import PySimpleGUI as sg

theme = sg.theme('DarkBrown7')

# Define the menu layout
menu_layout = [['File', ['Open', 'Save', 'Exit']]]

# Create the window layout
layout = [[sg.Menu(menu_layout)],
          [sg.Text('Selecione o seu filtro:')],
          [sg.Radio('Anos 60', "filtro", default=True), 
           sg.Radio('Anos 70', "filtro", default=False), 
           sg.Radio('Anos 80', "filtro", default=False), 
           sg.Radio('Anos 90', "filtro", default=False), 
           sg.Radio('Anos 2000', "filtro", default=False), 
           sg.Radio('Anos 2010', "filtro", default=False)]
]

# Create the window
window = sg.Window('Análise de Temperatura', layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

window.close()
