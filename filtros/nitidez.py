import cv2
import numpy as np

class FiltroNitidez:
    nome = 'Nitidez'

    def aplicar(self, img):
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        return cv2.filter2D(img, -1, kernel)
