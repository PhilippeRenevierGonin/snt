
# point d'entrée du script
if __name__ == '__main__':
    nbAllumettes = 20
    while nbAllumettes > 0:
        # todo : faire le tour de la personne qui joue
        if nbAllumettes > 0:
            coupO = 1
            print(f"L'ordinateur a choisi de prendre {coupO} allumettes")
            nbAllumettes = nbAllumettes - coupO
            print(f"Après le tour de l'ordinateur, il reste {nbAllumettes} allumettes")
            if nbAllumettes <= 0:
                print("désolé, vous avez perdu")
        else:
            print("bravo, vous avez gagné")


