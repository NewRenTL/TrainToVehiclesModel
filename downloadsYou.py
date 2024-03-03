from pytube import YouTube

# URL del video de YouTube
url = "https://www.youtube.com/watch?v=j5cSihIUc_o&ab_channel=Mr.Traphil"

# Directorio de descarga (puedes cambiarlo según tus necesidades)
download_path = "./"

# Crear un objeto YouTube
yt = YouTube(url)

# Obtener la stream de mayor resolución
video_stream = yt.streams.get_highest_resolution()

# Descargar el video
video_stream.download(download_path)

print(f"Video descargado en: {download_path}")
