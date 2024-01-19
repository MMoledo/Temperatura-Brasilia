import PySimpleGUI as sg

theme = sg.theme('DarkBrown7')

# Define the menu layout
menu_layout = [['File', ['Open', 'Save', 'Exit']],
               ['Edit', ['Cut', 'Copy', 'Paste']]]

# Create the window layout
layout = [[sg.Menu(menu_layout)],
          [sg.Text('Hello, world!')]]

# Create the window
window = sg.Window('Menu Example', layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

window.close()
