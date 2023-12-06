import PySimpleGUI as sg
import janela_solo as jsl
import janela_chuva as jch
sg.theme('LightBlue')

layout = [
    [sg.Button('Solo'), sg.Button('Praticas'), sg.Button('Chuva')]
]

window = sg.Window('Erosão do solo', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Solo':
        jsl.create_window()
    if event == 'Chuva':
        jch.create_window()
    if event == 'Praticas':
        pass

window.close()
