from random import shuffle

# Saisie d'une liste de mot avec le / en caractère de séparation --> en créer une liste
phrase = input(
    "Entré une liste de mot avec le caractère / en séparateur : ").split("/")
print("Liste d'origine {}".format(phrase))

# Mélanger cette liste
shuffle(phrase)
print("Liste shuffle {}".format(phrase))

if len(phrase) < 10:
    print("<10 donc : Element1 = {} & Element2 = {}".format(
        phrase[0], phrase[1]))
else:
    print(">10 donc : Dernier = {} & Avant dernier = {} & Avant avant dernier = {}".format(
        phrase[len(phrase)-1], phrase[len(phrase)-2], phrase[len(phrase)-3]))
