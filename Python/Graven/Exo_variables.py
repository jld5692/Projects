# code
wallet = 5000
computer_price = 6000

# le prix de l'ordinateur est inféreiru à 1000 euros
if computer_price <= wallet:
    print("Ready pour l'achat")
    wallet -= computer_price
    print("Il vous reste {} dans votre porte monnaie".format(wallet))
else:
    print("Pas assez d'argent sur le wallet")
    manque = computer_price - wallet
    print("Il vous manque {} euros dans votre wallet".format(manque))
