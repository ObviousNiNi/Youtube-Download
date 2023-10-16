from moviepy.editor import *
import os


from moviepy.editor import *
import os

def convert_to_mp3(video_file, to_mp3=False):
    mp3_file = None

    if to_mp3:
        # Obtén la ruta del archivo de salida en formato MP3
        mp3_file = os.path.splitext(video_file)[0] + ".mp3"

        # Carga el video original
        video = VideoFileClip(video_file)

        # Extrae la pista de audio y guárdala como archivo MP3
        audio = video.audio
        audio.write_audiofile(mp3_file)

        # Limpia y elimina el archivo de video original
        video.reader.close()
        audio.close()
        os.remove(video_file)

    return mp3_file
