from pytube import YouTube
from toMp3 import convert_to_mp3
import os

download_as_mp3 = False

def set_download_as_mp3(value):
    global download_as_mp3
    download_as_mp3 = value

def descargar_videos(url_entry, status_text):
    urls = url_entry.get("1.0", "end").strip().split('\n')
    for url in urls:
        url = url.strip()
        if url:
            try:
                yt = YouTube(url)
                video = yt.streams.get_highest_resolution()
                os.makedirs("Descargas", exist_ok=True)
                download_path = "Descargas"
                video_file = os.path.join(download_path, video.default_filename)
                video.download(download_path)

                if download_as_mp3:
                    mp3_file = convert_to_mp3(video_file, to_mp3=True)
                    mensaje = f"Descarga completada: {yt.title}.mp3"
                else:
                    mp3_file = None
                    mensaje = f"Descarga completada: {yt.title}.mp4"

                status_text.config(state="normal")
                status_text.insert("end", mensaje + "\n")
                status_text.see("end")
                status_text.config(state="disabled")
            except Exception as e:
                mensaje = f"Error en la URL: {url}"
                status_text.config(state="normal")
                status_text.insert("end", mensaje + "\n")
                status_text.see("end")
                status_text.config(state="disabled")
        else:
            mensaje = "Ingresa una URL válida"
            status_text.config(state="normal")
            status_text.insert("end", mensaje + "\n")
            status_text.see("end")
            status_text.config(state="disabled")


