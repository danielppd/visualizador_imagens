import cv2

class FiltroGrayscale:
    nome = 'Cinza'

    def aplicar(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
