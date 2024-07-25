# SNT, Activité 04 : écrire un script sur le jeu de Nim

Pour cette implémentation du programme conçu lors de l'activité précédente, nous allons simplifier le programme :
- en fixant que l'ordinateur choisit toujours de prendre une seule allumette à la fois
- en ne se préoccupant pas du pluriel ou du singulier lors des messages qui donnent le nombre d'allumettes

Voici un déroulé possible du programme : 

```
affecter 20 à nbAllumettes
boucle (tant que nbAllumettes > 0)
    afficher 'À vous de jouer, il reste {nbALlumettes} allumettes'
    demander le nombre d'allumettes prises (1, 2 ou 3) et l'affecter à coupJ
    calculer nbAllumettes - coupJ et l'affecter à nbALlumettes
    afficher 'Àprès votre tour, il reste {nbALlumettes} allumettes'
    si (nbAllumettes > 0)
        affecter 1 à coupO
        afficher 'L'ordinateur a choisi de prendre {coupO} allumettes'
        calculer nbAllumettes - coupO et l'affecter à nbALlumettes
        afficher 'Àprès le tour de l'ordinateur, il reste {nbALlumettes} allumettes'
        si (nbAllumettes <= 0)
            afficher "Vous avez perdu !"
    sinon
        afficher "Vous avez gagné !"
```

Pour cette activité, nous commencerons avec un [script qui ne fait que le tour de l'ordinateur](04_allumettes.py). 

## Prise en main du script fourni

### Exécutez le script dans Thonni. Combien de fois la boucle est-elle exécutée ? 
### Peut-on voir lors de l'exécution le message "Vous avez gagné !" ? 
### Est-ce que la boucle while présente dans le script peut être infinie dans l'état actuel du code ?
### Quelle partie du déroulé manque-t-il pour avoir le jeu "complet" ? 

## Faire le tour de la personne qui joue

### Complétez le code

Pour cela, il vous faut utiliser, au bon endroit, : 
- print() pour afficher les allumettes restantes, 
- input() et int() pour demander à la personne qui joue le nombre qu'elle choisit
- une soustraction à affecter à nbAllumettes
- print() pour afficher le nombre d'allumettes restantes après le coup qui vient d'être joué

### Est-ce que la boucle while présente dans le script peut être infinie dans l'état actuel du code ?

Essayez de jouer en saisissant -100 par exemple. 
Il s'agit ici que de constater, nous réglerons le problème plus tard. 


### Que se passe-t-il si vous tapez "un" ou lieu de 1 ?

Il s'agit ici que de constater, nous réglerons le problème plus tard. 


## S'assurer que la personne tape bien "1", "2" ou "3"

La fonction input() permet d'obtenir une chaine de caractères tapée par l'utilisateur·rice. Cette chaine peut être un "mot" ou un nombre ou "n'importe quoi", y compris une chaine vide. 
La fonction int() ne peut convertir que les chaines qui sont littéralements des nombres entiers. Dans notre cas, nous ne voulons que 3 cas particuliers : "1", "2", "3".
Il nous est donc possible de tester la chaine tapée avant de la convertir. Si elle correspond bien à "1", "2" ou "3", alors on peut convertir, sinon que faire ? 

### Quelles possibilités envisagez-vous ?

### Implémentez une possibilité simple : en cas d'erreur de saisie, attribuer arbitrairement la valeur 1 à coupJ

Pour cela, il faudra utiliser une expression booléenne avec 2 "or" (ou), car il y a 3 cas acceptés. 

### Proposez une correction si l'utilisateur·rice prend plus d'allumettes qu'il n'en reste (par exemple, il en reste 2, il en prend 3) ?


## Qu'est-ce qui pourrait être amélioré dans le programme ? 

Il s'agit ici de lister des pistes d'amélioration du programme, pour "voir" ce qu'il nous resterait à faire si nous voulions avoir un "produit fini".
Essayons de classer ces pistes en :
- ce qui nous est possible avec nos connaissances en python
- ce qui nous semble hors d'atteinte

