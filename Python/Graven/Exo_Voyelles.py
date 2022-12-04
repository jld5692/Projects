def get_vowels_numbers(mot):
    nb_vowels = 0   # on initialise le compteur
    # on va maintenant créer une liste contenant les voyelles
    list_vowels = ["a", "e", "i", "o", "u", "y"]

    for letter in mot:
        if letter in list_vowels:
            nb_vowels += 1

    print(mot)
    return nb_vowels


# Saisie d'un mot par l'utilisateur et appel ensuite à la fonction de comptage des voyelles
mot = input("Merci d'entrer un mot : ")
print("On a " + str(get_vowels_numbers(mot)) + " dans le mot " + mot)
