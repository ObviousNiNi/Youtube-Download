import os
from tkinter import *
from pytube import YouTube

# Función para descargar videos de YouTube en formato MP4
def descargar_videos():
    urls = url_entry.get("1.0", "end").strip().split('\n')
    for url in urls:
        url = url.strip()
        if url:
            try:
                yt = YouTube(url)
                video = yt.streams.get_highest_resolution()
                os.makedirs("Descargas", exist_ok=True)
                download_path = "Descargas"
                video.download(download_path)
                video_filename = video.default_filename
                mensaje = f"Descarga completada: {yt.title}.mp4"
                status_text.config(state="normal")
                status_text.insert("end", mensaje + "\n")
                status_text.see("end")  # Hacer scroll para mostrar el texto más reciente
                status_text.config(state="disabled")
            except Exception as e:
                mensaje = f"Error en la URL: {url}"
                status_text.config(state="normal")
                status_text.insert("end", mensaje + "\n")
                status_text.see("end")  # Hacer scroll para mostrar el texto más reciente
                status_text.config(state="disabled")
        else:
            mensaje = "Ingresa una URL válida"
            status_text.config(state="normal")
            status_text.insert("end", mensaje + "\n")
            status_text.see("end")  # Hacer scroll para mostrar el texto más reciente
            status_text.config(state="disabled")

# Configuración de la ventana
root = Tk()
root.title("Descargador de Videos de YouTube")
root.geometry("400x300")

# Área de texto para ingresar las URLs
url_label = Label(root, text="URLs de los videos (una por línea):")
url_label.pack(pady=10)
url_entry = Text(root, height=5, width=40)
url_entry.pack()

# Botón para iniciar la descarga
download_button = Button(root, text="Iniciar Descarga", command=descargar_videos)
download_button.pack(pady=10)

# Área de texto para mostrar el historial de descargas (solo de lectura)
status_text = Text(root, height=10, width=40, state="disabled")
status_text.pack()

# Iniciar la aplicación
root.mainloop()
