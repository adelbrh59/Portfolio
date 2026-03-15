# Créé par Adel, le 15/03/2026 en Python 3.
while True:
    nb1 = input("Entrez le premier nombre: ")
    if nb1.isdigit():
        nb1 = int(nb1)
        break
    else:
        print("Veuillez entrer un nombre valide.")

sgn = input("Entrez le signe (+, -, *, /): ")

while True:
    nb2 = input("Entrez le deuxieme nombre: ")
    if nb2.isdigit():
        nb2 = int(nb2)
        break
    else:
        print("Veuillez entrer un nombre valide.")

if sgn == '+':
    print(nb1 + nb2)

elif sgn == '-':
    print(nb1 - nb2)

elif sgn == '*':
    print(nb1 * nb2)

elif sgn == '/':
    print(nb1 / nb2)

else:
    print("Assurez vous d'avoir mis l'un de ces signes : + - * /")