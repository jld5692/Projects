from pytube import YouTube


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Problème lors du téléchargement de la vidéo !")
    print("Téléchargement terminé")


link = input("Entrer l'URL à tékécharger: ")
Download(link)
