from pytube import YouTube
from flask import request

link_video_conversao = ""
nome_arquivo = ""


def pegar_link_video():
    try:
        global link_video_conversao
        link_video_conversao = request.form.get("linkVideo")
        print(link_video_conversao)
        #baixar_audio(link_video_conversao)
        return baixar_audio(link_video_conversao)
    except Exception as e:
        print(e)
        return f"<p>Erro ao acessar f'{e}'</p>"


def baixar_audio(link_video):
    yt = YouTube(link_video, on_progress_callback=progress_function, on_complete_callback=on_completed)
    audio = yt.streams.filter(only_audio=True, )[0]
    audio.download()


def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(percentage_of_completion)


def on_completed(stream, file_path):
    print("dfsfd")
    retorno_pagina()


def retorno_pagina():
    return "Download Comcluido"
