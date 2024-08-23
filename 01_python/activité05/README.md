# SNT, Activité 05 : écrire des fonctions

Nous allons partir d'une version du jeu des allumettes pour en modifier le code en introduisant des fonctions. 
Nous commencerons avec un [script fourni qui oppose un humain à un ordi qui prend toujours une allumette](05_allumettes.py). 

Pour commencer, ignorons les fonctions "fonction1" et "fonction2"

## Question d'orthographe

Dans ce script, le mot "allumette" est toujours au pluriel, même s'il y en a 0 ou 1. L'objectif de cette question est d'avoir la bonne orthographe.

### Identifiez dans le code où "allumette" (avec ou sans "s") est affiché (print)

Parmi toutes ces utilisations, lesquelles concernent un nombre (potentiellement) variable d'allumettes ?

### Proposez un mini-algorithme pour détermines s'il faut écrire "allumette" ou "allumettes"

### Implémentez une fonction "formatage_nbAllumettes(nb)"

Cette fonction prend en paramètre un nombre d'allumettes et elle retourne : 
 - {nb} allumettes si nb >= 2
 - 1 allumette si nb = 1
 - 0 allumette si nb = 0

A-t-on besoin d'utiliser "elif" dans ce cas ?

### Utilisez la fonction "formatage_nbAllumettes" là où c'est nécessaire

Exécutez votre programme. Est-ce que maintenant "allumette" a la bonne marque du pluriel ou du singulier ?


## Variante de la fonction

Maintenant, nous voudrions que l'affichage du nombre d'allumettes changent en fonction du nombre : 
 - {nb} allumettes si nb >= 2, nb étant écrit en "chiffre"
 - "une seule allumette" si nb = 1 ("une" est écrit en toutes lettres)
 - zéro allumette si nb = 0 ("zéro" est écrit en toutes lettres)
 - 
A-t-on besoin d'utiliser "elif" dans ce cas ?

À combien d'endroit avez-vous modifié le code ? 

## Réfléchissons à un algorithme pour l'ordinateur (S'il reste du temps)

### Que jouer pour gagner à coup sûr ? 

Plutôt que de toujours prendre 1 allumette, l'ordinateur pourrait jouer plus intelligemment. Considérez les cas :
 - où il reste 3 allumettes : combien d'allumettes faut-il prendre pour gagner ? 
 - où il reste 2 allumettes : combien d'allumettes faut-il prendre pour gagner ? 
 - où il reste 1 allumette : combien d'allumette(s) faut-il prendre pour gagner ? 

S'il en reste entre 5 et 7, peut-on se ramener à aux 3 cas précédent, sachant que l'autre joueur prendre entre 1 et 3 allumettes ? 

Que peut-on dire s'il reste 4 ou 8 allumettes et que c'est à vous de jouer ? Quel choix peut-on faire ? 

### Généralisation et implémentation

Essayer de généraliser le principe (au pire considérer jusqu'à 20 allumettes).

Est-ce que dans le code fourni ce principe est implémenté ? Si oui, n'hésitez pas à renommer des fonctions ou des variables pour expliciter cette implémentation.

Est-ce que l'ordinateur qui joue ainsi peut-il perdre ? si oui, dans quelle condition ? 

### Mise en pratique

Modifiez le code pour jouer contre un ordinateur "fort".

Avez-vous modifié beaucoup de chose dans la boucle "while" ?

Essayez de gagner (en modifiant le nombre d'allumettes initial si nécessaire).
