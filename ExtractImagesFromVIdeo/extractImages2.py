import cv2
import os
import random
import numpy as np

def extract_frames(video_path, output_folder, num_frames):
    # Abre el archivo de video
    cap = cv2.VideoCapture(video_path)

    # Obtiene la frecuencia de fotogramas (fps) del video
    #fps = cap.get(cv2.CAP_PROP_FPS)

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Parámetro lambda para la distribución exponencial
    lambda_param = 0.5  # Puedes ajustar este valor según tus preferencias

    # Genera los tiempos seleccionados aleatoriamente con distribución exponencial
    selected_times = np.random.exponential(scale=lambda_param, size=num_frames)

    # Normaliza los tiempos al tiempo total del video
    selected_times = (selected_times / selected_times.sum()) * total_frames

    # Lista para almacenar los nombres de los archivos de imagen
    image_files = []

    # Itera sobre los fotogramas seleccionados
    for time in selected_times:
        # Establece el fotograma en la posición actual
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(time))

        # Lee el fotograma
        ret, frame = cap.read()

        if ret:
            # Genera un nombre de archivo único basado en el número de fotograma
            image_file = os.path.join(output_folder, f"frame_{int(time)}.jpg")

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
output_folder = './testimages2'

# Número total de imágenes deseadas
num_frames = 90

# Crea la carpeta de salida si no existe
if not os.path.exists(output_folder):
    print("not exists")
    os.makedirs(output_folder)

# Extrae las imágenes del video
extracted_images = extract_frames(video_path, output_folder, num_frames)

print(f"{num_frames} images extracted randomly from the video and saved in the output folder.")
