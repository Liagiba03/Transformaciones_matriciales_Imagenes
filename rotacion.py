import cv2
import numpy as np

image = cv2.imread('6.jpg')
ancho = image.shape[1]
alto = image.shape[0]

#ROTACION
M = cv2.getRotationMatrix2D((ancho//2,alto//2),15,1)
imageOut =  cv2.warpAffine(image,M,(ancho,alto))

cv2.imshow('Entrada',image)
cv2.imshow('Salida',imageOut)
cv2.waitKey(0)
cv2.destroyAllWindows()