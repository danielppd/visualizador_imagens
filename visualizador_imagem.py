import cv2
import PySimpleGUI as sg
from filtros import lista_filtros
from layout import layout, chaves_filtros

# Funções de transformação independentes

def rotacionar(img, angulo):
    h, w = img.shape[:2]
    M = cv2.getRotationMatrix2D((w/2, h/2), angulo, 1)
    return cv2.warpAffine(img, M, (w, h))


def redimensionar(img, largura, altura):
    return cv2.resize(img, (largura, altura), interpolation=cv2.INTER_AREA)

# Inicialização da GUI
janela = sg.Window('Visualizador de Imagens', layout)
img_original = None
img_resultado = None

while True:
    evento, valores = janela.read()
    if evento in (sg.WIN_CLOSED, 'Exit'):
        break

    if evento == 'Carregar Imagem':
        caminho = sg.popup_get_file('Escolha uma imagem', file_types=(('PNG', '*.png'), ('JPEG', '*.jpg;*.jpeg'), ('Todos', '*.*')))
        if caminho:
            img_original = cv2.imread(caminho)
            img_resultado = img_original.copy()
            dados = cv2.imencode('.png', img_original)[1].tobytes()
            janela['-ORIGINAL-'].update(data=dados)
            janela['-RESULTADO-'].update(data=dados)

    if evento == 'Resetar' and img_original is not None:
        img_resultado = img_original.copy()
        dados = cv2.imencode('.png', img_resultado)[1].tobytes()
        janela['-RESULTADO-'].update(data=dados)

    # Aplicar filtros
    if img_original is not None and evento in chaves_filtros:
        filtro = next(f for f in lista_filtros if f.nome == evento)
        img_resultado = filtro.aplicar(img_resultado)
        dados = cv2.imencode('.png', img_resultado)[1].tobytes()
        janela['-RESULTADO-'].update(data=dados)

    # Aplicar transformações
    if img_original is not None and evento == 'Rotacionar':
        angulo = float(sg.popup_get_text('Ângulo de rotação (graus):', default_text='90'))
        img_resultado = rotacionar(img_resultado, angulo)
        janela['-RESULTADO-'].update(data=cv2.imencode('.png', img_resultado)[1].tobytes())
    
    if img_original is not None and evento == 'Redimensionar':
        l, a = map(int, sg.popup_get_text('Largura,Altura:', default_text='800,600').split(','))
        img_resultado = redimensionar(img_resultado, l, a)
        janela['-RESULTADO-'].update(data=cv2.imencode('.png', img_resultado)[1].tobytes())

    if evento == 'Salvar Resultado' and img_resultado is not None:
        destino = sg.popup_get_file('Salvar como', save_as=True, file_types=(('PNG', '*.png'), ('JPEG', '*.jpg;*.jpeg')))
        if destino:
            cv2.imwrite(destino, img_resultado)
            sg.popup('Imagem salva em:', destino)

janela.close()
