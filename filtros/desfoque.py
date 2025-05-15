import cv2

class FiltroDesfoque:
    nome = 'Desfoque'

    def __init__(self, ksize=5):
        self.ksize = ksize

    def aplicar(self, img):
        return cv2.GaussianBlur(img, (self.ksize, self.ksize), 0)
