def fonction1(nbAll):
    return 1;

def fonction2(nbAll):
    coup = 1;
    if (nbAll % 4 > 0):   # % = modulo (reste de la division entière)
        coup = nbAll - (nbAll // 4)*4   # // = division entière (le résultat est un entier : a = (a//b) * b + a%b  )
    return coup

if __name__ == '__main__':
    nbAllumettes = 20
    print(f"il y a {nbAllumettes} allumettes")
    while nbAllumettes > 0:
        coupJoueur = input("Combien d'allumettes prenez-vous ? 1, 2 ou 3 : ")
        if coupJoueur == "1" or coupJoueur == "2" or coupJoueur == "3":
            coupJoueur = int(coupJoueur)
            if (coupJoueur > nbAllumettes):
                coupJoueur = nbAllumettes
        else:
            coupJoueur = 1
        nbAllumettes = nbAllumettes - coupJoueur
        print(f"Après votre tour, il reste {nbAllumettes} allumettes")
        if nbAllumettes > 0:
            coupOrdi = 1
            print(f"L'ordinateur a choisi de prendre {coupOrdi} allumettes")
            nbAllumettes = nbAllumettes - coupOrdi
            print(f"Après le tour de l'ordinateur, il reste {nbAllumettes} allumettes")
            if nbAllumettes <= 0:
                print("désolé, vous avez perdu")
        else:
            print("bravo, vous avez gagné")