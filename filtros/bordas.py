import cv2

class FiltroBordas:
    nome = 'Bordas'

    def aplicar(self, img):
        cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        bordas = cv2.Canny(cinza, 100, 200)
        return cv2.cvtColor(bordas, cv2.COLOR_GRAY2BGR)
