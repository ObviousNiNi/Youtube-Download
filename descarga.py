from pytube import YouTube
import os


def descargar_videos(url_entry, status_text):
    # Obtenemos el contenido del campo de entrada de URL y lo dividimos en una lista de URLs
    urls = url_entry.get("1.0", "end").strip().split('\n')

    # Iteramos a través de cada URL proporcionada
    for url in urls:
        # Eliminamos cualquier espacio en blanco al comienzo o final de la URL
        url = url.strip()

        # Verificamos si la URL es válida
        if url:
            try:
                # Creamos una instancia de YouTube para la URL
                yt = YouTube(url)

                # Obtenemos la mejor calidad de video disponible para la descarga
                video = yt.streams.get_highest_resolution()

                # Creamos un directorio 'Descargas' si no existe
                os.makedirs("Descargas", exist_ok=True)
                download_path = "Descargas"

                # Descargamos el video en la ubicación especificada
                video.download(download_path)

                # Obtenemos el nombre de archivo predeterminado del video descargado
                video_filename = video.default_filename

                # Mostramos un mensaje en el área de texto de estado
                mensaje = f"Descarga completada: {yt.title}.mp4"
                status_text.config(state="normal")
                status_text.insert("end", mensaje + "\n")
                status_text.see("end")  # Desplazamos hacia la última línea
                status_text.config(state="disabled")  # Bloqueamos el área de texto

            except Exception as e:
                # Si ocurre un error, mostramos un mensaje de error en el área de texto de estado
                mensaje = f"Error en la URL: {url}"
                status_text.config(state="normal")
                status_text.insert("end", mensaje + "\n")
                status_text.see("end")
                status_text.config(state="disabled")
        else:
            # Si la URL está en blanco, mostramos un mensaje de error en el área de texto de estado
            mensaje = "Ingresa una URL válida"
            status_text.config(state="normal")
            status_text.insert("end", mensaje + "\n")
            status_text.see("end")
            status_text.config(state="disabled")

