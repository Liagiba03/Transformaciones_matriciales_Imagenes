import cv2
import numpy as np

image = cv2.imread('6.jpg')
ancho = image.shape[1]
alto = image.shape[0]

#ESCALAMIENTO
imageOut = cv2.resize(image,(600,100),interpolation = cv2.INTER_CUBIC)

cv2.imshow('Entrada',image)
cv2.imshow('Salida',imageOut)
cv2.waitKey(0)
cv2.destroyAllWindows()