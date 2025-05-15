import PySimpleGUI as sg
from filtros import lista_filtros

chaves_filtros = [filtro.nome for filtro in lista_filtros]

layout = [
    [sg.Text('Visualizador de Imagens', font=('Any', 16))],
    [sg.Button('Carregar Imagem'), sg.Button('Salvar Resultado'), sg.Button('Resetar')],
    [sg.Image(key='-ORIGINAL-'), sg.Image(key='-RESULTADO-')],
    [sg.Text('Filtros:')] + [sg.Button(nome) for nome in chaves_filtros],
    [sg.Text('Transformações:'), sg.Button('Rotacionar'), sg.Button('Redimensionar')]
]