from os import path
from random import choice

if path.exists("meals.txt"):
    # On lance le script
    with open("meals.txt", "r+") as file:
        meal_list = file.readlines()
        meal_random_choice = choice(meal_list)
        print(meal_random_choice)
    file.close() 
else:
    print("Fichier introuvable") 