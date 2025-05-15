import cv2

class FiltroContraste:
    nome = 'Contraste'

    def __init__(self, alpha=1.5, beta=0):
        self.alpha = alpha
        self.beta = beta

    def aplicar(self, img):
        return cv2.convertScaleAbs(img, alpha=self.alpha, beta=self.beta)
