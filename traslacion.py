import cv2
import numpy as np

image = cv2.imread('6.jpg')
ancho = image.shape[1]
alto = image.shape[0]

#TRASLACIÓN
M = np.float32([[1,0,10],[0,1,100]])
imageOut =  cv2.warpAffine(image,M,(ancho,alto))

cv2.imshow('Entrada',image)
cv2.imshow('Salida',imageOut)
cv2.waitKey(0)
cv2.destroyAllWindows()