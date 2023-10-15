import os
from tkinter import *
from pytube import YouTube
from PIL import Image, ImageDraw
from ttkthemes import ThemedStyle



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

# Función para crear un fondo degradado con Pillow
def crear_fondo_degradado(width, height):
    fondo = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(fondo)

    start_color = (0x33, 0x33, 0x33)  # Color #333333
    end_color = (0x1a, 0x2e, 0x38)  # Color #1a2e38

    for y in range(height):
        # Calcular el color en función de la posición vertical
        r = start_color[0] + (end_color[0] - start_color[0]) * y // height
        g = start_color[1] + (end_color[1] - start_color[1]) * y // height
        b = start_color[2] + (end_color[2] - start_color[2]) * y // height
        color = (r, g, b)
        draw.line([(0, y), (width, y)], fill=color)

    return fondo

# Guardar el fondo degradado en un archivo
def guardar_fondo_degradado(fondo_degradado, filename):
    fondo_degradado.save(filename, "PNG")



# Configuración de la ventana
root = Tk()
root.title("Descargador de Videos de YouTube")
root.geometry("800x400")
# Impedir que la ventana sea redimensionable
root.resizable(False, False)  # (Ancho, Alto)



# Crear un fondo degradado de 800x400 con Pillow
fondo_degradado = crear_fondo_degradado(800, 400)

# Guardar el fondo degradado en un archivo PNG
guardar_fondo_degradado(fondo_degradado, "background.png")

# Cargar el fondo desde el archivo en un Canvas
photo = PhotoImage(file="background.png")
background_canvas = Canvas(root, width=800, height=400)
background_canvas.create_image(0, 0, anchor="nw", image=photo)
background_canvas.place(x=0, y=0, relwidth=1, relheight=1)  # Coloca el Canvas en toda la ventana

style = ThemedStyle(root)
style.set_theme("equilux")


# Área de texto para ingresar las URLs
url_label = Label(root, text="URLs de los videos (una por línea):",
                  fg="#cececa", bg="#333333", relief="groove", borderwidth=0.6)
url_label.place(x=10, y=10)  # Ajusta la posición a tu preferencia

url_entry = Text(root, height=12.5, width=85, bg="#2e4041", fg="#cececa")
url_entry.place(x=10, y=40)  # Ajusta la posición a tu preferencia


# Botón para iniciar la descarga
dwnd = PhotoImage(file='download.png')
dwnd = dwnd.subsample(10)
download_button = Button(root, image=dwnd, command=descargar_videos,
                         borderwidth=0, background="#2e4041", relief="flat",
                         activebackground='#404c48', activeforeground='white')
download_button.place(x=720, y=120)  # Ajusta la posición a tu preferencia

# Área de texto para mostrar el historial de descargas (solo de lectura)
status_text = Text(root, height=7, width=85, state="disabled",
                   font=("Consolas", 12), bg="#2e4041", fg="#cececa")
status_text.place(x=10, y=260)  # Ajusta la posición a tu preferencia



# Iniciar la aplicación
root.mainloop()
