from pytube import YouTube


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path="C:\Temp")
    except:
        print("Problème lors du téléchargement de la vidéo !")
    print("Téléchargement terminé")


URL_YT = input("Entrer l'URL à tékécharger: ")
Download(URL_YT)
