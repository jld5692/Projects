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
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil


# Functions
def select_path():
    # allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_file():
    # get user path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    # Download Video --> on pourrait améliorer le prog en laissant l'utilisateur choisir la qualité
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    # move file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete! Download Another File...')


screen = Tk()
title = screen.title('Youtube Download')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

# Logo YT en ipmage --> à voir de plus prêt car on n'est pas sur un chemin relatif
logo_img = PhotoImage(file='C:\\Projects\\Utils\\Youtube\\yt.png')
# resize
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 80, image=logo_img)

# link field
link_field = Entry(screen, width=40, font=('Arial', 15))
link_label = Label(screen, text="Lien YT à télécharger: ", font=('Arial', 15))

# Select Path for saving the file
path_label = Label(
    screen, text="Chemin cible du fichier télécharger", font=('Arial', 15))
select_btn = Button(screen, text="Path", bg='red', padx='22',
                    pady='5', font=('Arial', 15), fg='#fff', command=select_path)
# Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

# Add widgets to window
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

# Download btns
download_btn = Button(screen, text="Download File", bg='green', padx='22',
                      pady='5', font=('Arial', 15), fg='#fff', command=download_file)
# add to canvas
canvas.create_window(250, 390, window=download_btn)

screen.mainloop()
