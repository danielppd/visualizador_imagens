import cv2

class FiltroInverter:
    nome = 'Inverter'

    def aplicar(self, img):
        return cv2.bitwise_not(img)
