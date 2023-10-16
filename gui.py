from tkinter import *
from PIL import Image, ImageDraw
from ttkthemes import ThemedStyle
from descarga import descargar_videos  # Importa la función de descarga desde descarga.py
from descarga import set_download_as_mp3  # Importa la función de descarga mp3 desde descarga.py


# Función para crear un fondo degradado usando la biblioteca Pillow
def crear_fondo_degradado(width, height):
    fondo = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(fondo)

    start_color = (0x33, 0x33, 0x33)  # Color #333333
    end_color = (0x1a, 0x2e, 0x38)  # Color #1a2e38

    for y in range(height):
        # Calcula el color en función de la posición vertical
        r = start_color[0] + (end_color[0] - start_color[0]) * y // height
        g = start_color[1] + (end_color[1] - start_color[1]) * y // height
        b = start_color[2] + (end_color[2] - start_color[2]) * y // height
        color = (r, g, b)
        draw.line([(0, y), (width, y)], fill=color)

    return fondo

#  Función para guardar el fondo degradado en un archivo
def guardar_fondo_degradado(fondo_degradado, filename):
    fondo_degradado.save(filename, "PNG")

# Crear una ventana principal de Tkinter
root = Tk()
root.title("Descargador de Videos de YouTube")
root.geometry("800x400")
root.resizable(False, False)
root.iconbitmap("imgs/youtube-play-button-outlined-social-symbol_icon-icons.com_74040.ico")


# Crear un fondo degradado y guardarlo en un archivo
fondo_degradado = crear_fondo_degradado(800, 400)
guardar_fondo_degradado(fondo_degradado, "background.png")

# Cargar el fondo desde el archivo en un lienzo (Canvas)
photo = PhotoImage(file="background.png")
background_canvas = Canvas(root, width=800, height=400)
background_canvas.create_image(0, 0, anchor="nw", image=photo)
background_canvas.place(x=0, y=0, relwidth=1, relheight=1)

# Estilo temático para la ventana
style = ThemedStyle(root)
style.set_theme("equilux")

# Etiqueta para la entrada de URLs
url_label = Label(root, text="URLs de los videos (una por línea):",
                  fg="#cececa", bg="#333333", relief="groove", borderwidth=0.6)
url_label.place(x=10, y=10)

# Campo de entrada de URLs
url_entry = Text(root, height=12.5, width=85, bg="#2e4041", fg="#cececa")
url_entry.place(x=10, y=40)

# Botón para iniciar la descarga
dwnd = PhotoImage(file='imgs/mp4.png')
dwnd = dwnd.subsample(10)
download_button = Button(root, image=dwnd, command=lambda: descargar_videos(url_entry, status_text),
                         borderwidth=0, background="#2e4041", relief="flat",
                         activebackground='#404c48', activeforeground='white')
download_button.place(x=705, y=80)

# Botón para iniciar la descarga mp3
dwndmp3 = PhotoImage(file='imgs/mp3.png')
dwndmp3 = dwndmp3.subsample(6)
downloadmp3_button = Button(root, image=dwndmp3, command=lambda: [set_download_as_mp3(True),
                                                                  descargar_videos(url_entry, status_text)],
                         borderwidth=0, background="#2e4041", relief="flat",
                         activebackground='#404c48', activeforeground='white')
downloadmp3_button.place(x=705, y=150)

# Área de texto para mostrar el historial de descargas (solo de lectura)
status_text = Text(root, height=7, width=85, state="disabled",
                   font=("Consolas", 12), bg="#2e4041", fg="#cececa")
status_text.place(x=10, y=260)


# Iniciar la aplicación y abrir la ventana principal
root.mainloop()
