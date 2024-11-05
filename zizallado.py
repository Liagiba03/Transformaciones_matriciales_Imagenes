import cv2

image = cv2.imread('6.jpg')
print("image.shape = ",image.shape)

#ZIZALLADO
imageOut = image[10:100,100:50]

cv2.imshow('Entrada',image)
cv2.imshow('Salida',imageOut)
cv2.waitKey(0)
cv2.destroyAllWindows()