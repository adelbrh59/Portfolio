# Créé par Adel, le 15/03/2026 en Python 3.7
import random

nombre_secret = random.randint(1, 100)
tentatives = 0

print("Bienvenue dans le jeu du nombre mystère !")
print("Je pense à un nombre entre 1 et 100.")

while True:
    entree = input("Entre un nombre : ")

    if not entree.isdigit():
        print("Merci d'entrer un nombre valide.")
        continue

    proposition = int(entree)
    tentatives += 1

    if proposition < nombre_secret:
        print("Trop petit !")
    elif proposition > nombre_secret:
        print("Trop grand !")
    else:
        print("Bravo ! Tu as trouvé le nombre mystère.")
        print("Nombre de tentatives :", tentatives)
        break