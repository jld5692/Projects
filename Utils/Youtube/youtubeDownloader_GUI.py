# ---------------------------------------------------------------------------------------------------
# GUI pour télécharger des vidéos sur Youtube
# Pas mal d'optimation possible
#   - Passer en exécutable
#   - Choisir la qualité de téléchargement
#   - Barre d'avancement du téléchargement
#   - Message de fin de téléchargement avec temps, status, ...
#   - Et pourquoi pas un JSON pour le param par défaut avec possibilité d'avoir un fichier de log
# ---------------------------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
from pytube import Playlist

import shutil

##########################################################################

previousprogress = 0


def on_progress(stream, chunk, bytes_remaining):
    global previousprogress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining

    liveprogress = (int)(bytes_downloaded / total_size * 100)
    if liveprogress > previousprogress:
        previousprogress = liveprogress

        progress_bar = ttk.Progressbar(screen, orient='horizontal',
                                       mode='determinate', value=previousprogress, length=350)
        canvas.create_window(250, 450, window=progress_bar)
        value_label = ttk.Label(
            screen, text="Progression: "+str(previousprogress)+"%")
        canvas.create_window(250, 480, window=value_label)
        canvas.update()
##########################################################################


def select_path():
    # choix du chemin destination
    path = filedialog.askdirectory()
    # on viens mettre à jour dans la fenêtre le chemin choisi
    path_label.config(text=path)


def download_file():
    # get user path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget("text")
    screen.title('Downloading...')

    # On va afficher ici une barre de progression pour l'initialisation ( à voir si utile - premier refresh suffisant ?)
    progress_bar = ttk.Progressbar(screen, orient='horizontal',
                                   mode='determinate', length=350)
    canvas.create_window(250, 450, window=progress_bar)

    # permet de refresher la page et d'afficher du coup la progress bar.
    canvas.update()

#######################################################################################
    mp4_video = YouTube(get_link)
    mp4_video.register_on_progress_callback(on_progress)
    vid = mp4_video.streams.get_highest_resolution().download()
    # mp4_video.streams.filter(only_audio=True).first().download()
    vid_clip = VideoFileClip(vid)
    vid_clip.close()
    # on recopie le fichier téléchargé dans le répertoire cible
    shutil.move(vid, user_path)
    screen.title('Téléchargement terminé ! Bordel ca marche !!!')
#######################################################################################


# Début du programme >>>
screen = Tk()
# titre de la fenêtre (en haut à gauche)
title = screen.title('Youtube Downloader')
# fenêtre qui hébergera l'ensemble
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

# Logo YT en ipmage --> à voir de plus prêt car on n'est pas sur un chemin relatif
logo_img = PhotoImage(file='C:\\Projects\\Utils\\Youtube\\yt.png')
# resize
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 80, image=logo_img)

# ----------<
# zone de saisie pour le lien YT
link_field = Entry(screen, width=40, font=('Arial', 15))
link_label = Label(screen, text="Lien YT à télécharger: ", font=('Arial', 15))
# ----------<
# Choix du chemin de sauvegarde
path_label = Label(
    screen, text="Chemin cible du fichier télécharger", font=('Arial', 15))
select_btn = Button(screen, text="Path", bg='red', padx='22',
                    pady='5', font=('Arial', 15), fg='#fff', command=select_path)
# ----------<
# On ajoute à la fenêtre les éléments précédents
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)
# ----------<
# Bouton de téléchargement
download_btn = Button(screen, text="Download File", bg='green', padx='22',
                      pady='5', font=('Arial', 15), fg='#fff', command=download_file)
canvas.create_window(250, 390, window=download_btn)

# On lance l'affichage de la fenêtre avec tout ce qui a été préparé avant
# Et attends ensuite l'intéraction avec l'utilisateur
screen.mainloop()
