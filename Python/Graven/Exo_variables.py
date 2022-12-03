def main():
    # recolter une valeur de porte monnaie
    # creer un produit qui aura pour vakeur 50
    # afficher la n ouvelle valeur du porte monnaie, après son achat

    wallet = 200
    productName = "chocolat"
    productPrice = 50

    print("Bienvenue à la chocolaterie de Suresnes")
    nbBoite = int(input("Combien de boite souhaitez-vous acheter : "))

    ticketPrice = nbBoite * productPrice

    print("Pour " + str(nbBoite) + " vous nous devez " +
          str(ticketPrice) + " euros")

    print("--------------------------------------")
    wallet = wallet - ticketPrice
    print("il vous reste alors " + str(wallet) +
          " euros dans votre porte monnaie.")
    print("--------------------------------------")


if __name__ == '__main__':
    main()
