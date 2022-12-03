def main():
    # récupération de la première note
    note1 = int(input("Entrer la première note : "))
    note2 = int(input("Entrer la deuxième note : "))
    note3 = int(input("Entrer la troisième note : "))

    result = (note1 + note2 + note3) / 3
    print("La moyenne de l'élève est de : " + str(result))


if __name__ == '__main__':
    main()
