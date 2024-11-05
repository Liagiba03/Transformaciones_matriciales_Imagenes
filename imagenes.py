
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def apply_transformation(image, matrix):
    """Aplica una transformación a una imagen usando una matriz de transformación homogénea."""
    image_np = np.array(image)
    rows, cols = image_np.shape[:2]
    new_image = np.zeros_like(image_np)
    
    # Definir la matriz de transformación homogénea
    matrix_homogeneous = np.eye(3)
    matrix_homogeneous[:2, :2] = matrix[:2, :2]
    matrix_homogeneous[:2, 2] = matrix[:2, 2]
    
    # Recorre cada píxel de la nueva imagen y aplícale la transformación
    for x in range(rows):
        for y in range(cols):
            vec = np.array([x, y, 1])
            new_x, new_y, _ = matrix_homogeneous @ vec
            new_x, new_y = int(new_x), int(new_y)
            if 0 <= new_x < rows and 0 <= new_y < cols:
                new_image[new_x, new_y] = image_np[x, y]
    
    return Image.fromarray(new_image)

def rotate_image(image, angle):
    theta = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0,             0,             1]
    ])
    return apply_transformation(image, rotation_matrix)

def translate_image(image, tx, ty):
    translation_matrix = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])
    return apply_transformation(image, translation_matrix)

def shear_image(image, kx, ky):
    shear_matrix = np.array([
        [1, kx, 0],
        [ky, 1, 0],
        [0, 0, 1]
    ])
    return apply_transformation(image, shear_matrix)

def scale_image(image, sx, sy):
    scaling_matrix = np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])
    return apply_transformation(image, scaling_matrix)

# Cargar imagen
image = Image.open("6.jpg")

# Aplicar transformaciones
rotated_image = rotate_image(image, 45)  # Rotar 45 grados
translated_image = translate_image(image, 100, 50)  # Traslación de 100 píxeles en x y 50 en y
sheared_image = shear_image(image, 0.5, 0.5)  # Cizallamiento
scaled_image = scale_image(image, 1.5, 1.5)  # Escalamiento (1.5x en x y 1.5x en y)

# Mostrar imágenes
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.title('Rotación')
plt.imshow(rotated_image)
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Traslación')
plt.imshow(translated_image)
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Zizallado')
plt.imshow(sheared_image)
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('Escalamiento')
plt.imshow(scaled_image)
plt.axis('off')

plt.show()