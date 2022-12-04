# Recolter l'age de la personne"
age = int(input("Quel est votre age ? "))
ticketPrice = 0  # juste pour initialiser le prix du ticket de cinema

# Calcul de la place en fonction de l'age fourni précédemment par la personne
if age < 18:
    ticketPrice = 7
else:
    ticketPrice = 12

# On demande en plus s'il souhaite ou pas du pop corn à 5 euros
popCorn = str(input("Voulez vous en plus du pop corn ? (o/n)"))
if popCorn == "o" or popCorn == "O":
    ticketPrice += 5

print("Le prix a payer est de {} euros pour votre place de cinema".format(ticketPrice))
