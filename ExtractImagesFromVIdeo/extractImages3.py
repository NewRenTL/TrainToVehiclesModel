import cv2
import os
import random
import numpy as np

def extract_frames(video_path, output_folder, num_frames):
    # Abre el archivo de video
    cap = cv2.VideoCapture(video_path)

    # Obtiene el número total de fotogramas en el video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Lista para almacenar los nombres de los archivos de imagen
    image_files = []

    # Selecciona aleatoriamente 'num_frames' fotogramas de diferentes partes del video
    for _ in range(num_frames):
        # Establece el fotograma en una posición aleatoria
        random_frame = random.randint(0, total_frames - 1)
        cap.set(cv2.CAP_PROP_POS_FRAMES, random_frame)

        # Lee el fotograma
        ret, frame = cap.read()

        if ret:
            # Genera un nombre de archivo único basado en la posición actual
            image_file = os.path.join(output_folder, f"frame_{random_frame}.jpg")

            # Guarda el fotograma como una imagen
            cv2.imwrite(image_file, frame)

            # Agrega el nombre del archivo a la lista
            image_files.append(image_file)

    # Libera el objeto de captura
    cap.release()

    return image_files

# Ruta del archivo de video
video_path = 'C:/Users/Sierpe/Documents/ProjectTraffic/Assigment1/DataSet_TrainSet/traffic.mp4'

# Carpeta de salida para las imágenes
output_folder = './testimages3'

# Número total de imágenes deseadas
num_frames = 90

# Crea la carpeta de salida si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Extrae las imágenes del video
extracted_images = extract_frames(video_path, output_folder, num_frames)

print(f"{num_frames} images extracted randomly from different parts of the video and saved in the output folder.")
