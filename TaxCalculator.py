
age = int(input("Veuillez entrer l'âge de l'habitant : "))
sexe = input("Veuillez entrer le sexe de l'habitant (H pour homme et F pour femme) : ")


if (sexe == 'H' and age > 20) or (sexe == 'F' and age >= 18 and age <= 35):
    print("Cet habitant est imposable.")
else:
    print("Cet habitant n'est pas imposable.")
