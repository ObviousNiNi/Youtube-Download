# Descarga videos de YouTube

Este proyecto te permite descargar videos de YouTube de una manera sencilla utilizando una interfaz gráfica de usuario (GUI) construida con la biblioteca Tkinter de Python. Puedes ingresar las URLs de los videos que desees descargar, y el programa se encargará del proceso de descarga y conversión, permitiéndote guardar los videos en tu computadora.

## Cómo funciona

El proyecto consta de dos partes principales: la interfaz gráfica de usuario (GUI) y la lógica de descarga.

### Interfaz gráfica de usuario (GUI)

La interfaz gráfica te proporciona una forma amigable de interactuar con el programa. Puedes ingresar las URLs de los videos en un campo de texto y utilizar botones para iniciar las descargas. Además, se proporciona una sección donde podrás ver el historial de tus descargas (se reinicia al cerrar el programa).

### Lógica de descarga

La lógica de descarga se encarga de procesar las URLs proporcionadas y descargar los videos correspondientes desde YouTube. El programa utiliza la biblioteca `pytube` para obtener la mejor calidad de video disponible para cada URL y guarda los archivos descargados en una carpeta llamada "Descargas" en tu computadora. Si deseas, también puedes configurar el programa para descargar los videos como archivos MP3.

## Requisitos previos

Antes de utilizar este proyecto, asegúrate de tener Python instalado en tu computadora. También necesitarás instalar las siguientes bibliotecas:

- pytube: Para la descarga de videos de YouTube
- Pillow: Para la creación de elementos gráficos

Puedes instalar estas bibliotecas utilizando `pip`:

```bash
pip install pytube Pillow
pip install ttkthemes
pip install moviepy


