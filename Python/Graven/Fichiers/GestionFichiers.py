from os import system

# Ajout d'un étudiant à la liste existante
def add_student(new_student):
    with open("student.txt", "a+") as file:
        file.write(new_student + "\n")
        file.close()
    return

# Fonction de lecture complète de la liste des étudiants
def read_file():
    with open("student.txt", "r+") as file:
        student_list = file.readlines()
        print("Il y a " + str(len(student_list)) + " étudiant dans le fichier")
        cpt_student = 0
        while cpt_student < int(len (student_list)):
            print(str(cpt_student) + " : " + student_list[cpt_student])
            cpt_student += 1
    file.close() 

# Fonction de purge de la liste des étudiants --> à écrire
def purge_file():
    with open("student.txt", "r+") as file:
        print("A construire")
    file.close() 

# Fonction de purge de la liste des étudiants --> à écrire
def supp_student():
    with open("student.txt", "r+") as file:
            print("A construire")
    file.close() 

##################################################################################################
# On commence par nettoyer la console
system('cls')

print("--------------------------------------")
print("Bienvenue sur la gestion des étudiants")
print("--------------------------------------")
print("Actions possibles")
print("   1 - Ajouter un étudiant")
print("   2 - Afficher la liste des étudiants")

choice = input("Votre choix : ")

# En fonction du choix utilisateur, on va déclencher un traitement
match int(choice):
    case 1:
        # On ajout un étudiant en fichier
        nom_student = input("Ajouter un nom d'étudiant : ")
        add_student(nom_student)
    case 2:
        read_file()
    case _:
        print("It's bad !!!")
##################################################################################################
print("--------------------------------------")
print("THE END, THIS IS THE END")
print("--------------------------------------")
