# Activité 7 : manipulation des données avec Python

Pour commencer, récupérez [le code de base, lectureCSV.py](lectureCSV.py).

Si vous ne l'avez pas concervé, récupérer [le fichier des naissances de 2021](FD_NAIS_2021.csv).

En parallèle du code python ouvert dans Thonny, vous pouvez ouvrir le fichier dans excel et consulter la [définition des variables dans le fichier de référence](https://www.insee.fr/fr/statistiques/fichier/6652024/Contenu_etatcivil2021_nais2021.pdf) : 

**Sur une feuille que vous rendrez à la fin de l'activité, répondez aux questions suivantes.**

## Lecture du code fourni 

le code fourni est assez court : 
 - il commence par "import csv". Ceci permet de dire que le programme va utiliser une bibliothèque pour lire les fichiers csv. 
 - il y a ensuite une fonction dont le nom est "recommencerLectureDonnees", nous verrons par la suite son utilité et ce qu'est une fonction en python
 - puis il y a le programme principal (la partie "main"). Celle-ci permet au programme de consulter (= ouvrir) le contenu du fichier FD_NAIS_2021.csv. Puis à la fin, le programme referme le fichier. 

### 1. Rappelez ce qu'est un fichier csv. 
### 2. Recherchez et notez la notion de bibliothèque en programmation. 

## Exploiter les données en python : lire une ligne

Le code à écrire devra se faire dans la partie "main", mais avant "fichierSource.close()"

Pour les lire les valeurs du fichier, il y a 2 façons : 
 - lire la prochaine ligne :
```python
    premiereLigne = next(donnees)
```
 - faire une itération sur les données 
```python
    for ligne in donnees:
        #traitement d'une ligne après l'autre...
```

Commençons par la première : ajoutez dans votre code : 
```python
    premiereLigne = next(donnees)
    print(premiereLigne[0], premiereLigne[1], premiereLigne[2])
```   
### 3. Exécutez le programme, que voyez-vous dans la console ? Que contient premiereLigne ? 
### 4. Ajoutez à nouveau ces deux lignes à la suite des deux précédentes. Que voyez-vous dans la console ? Que contient maintenant premiereLigne ? Porte-t-elle bien son nom dans ce cas ?
### 5. Pour la ligne actuelle, (celle qui est dans la variable premiereLigne) affichez l'age de la maman, le département où a eu lieu la naissance et le sexe de l'enfant (1 pour un garçon, 2 pour une fille). Notez sur votre feuille comment vous avez fait.


## Exploiter les données en python : âge moyen des mères et nombre de filles 

Lorsque l'on a déjà lu une partie des données, pour recommencer à lire les données depuis le début, il suffit d'appeler la fonction recommencerLectureDonnees. Il vous revient de l'appeler lorsque cela est nécessaire. 

### 6. Faites une boucle "for" (c.f. faire une itération sur les données ci-dessus) pour calculer l'âge moyen des mères. Notez l'algorithme sur votre feuille. Notez aussi l'age moyen sur votre feuille. 
### 7. Complétez votre boucle pour savoir quel est l'âge de la plus jeune maman et celui de la plus vieille. Notez comment vous faites sur votre feuille et les résultats sur votre feuille. 

### 8. Faites une deuxième boucle pour compter le nombre de filles nées en 2021 et pour en calculer le pourcentage sur le total des naissances. Quelle est la formule pour calculer le pourcentage ? Combien trouvez-vous ?

### 9. Estimez le temps d'exécution de votre programme avec les deux boucles (par exemple en chronométrant avec un "téléphone" ou une montre). Fusionnez les deux boucles (et les calculs doivent encore fonctionner) et estimez à nouveau votre temps. Que constatez-vous ? Comment l'expliquer ?


## Exploiter les données en python : naissances dans la Drôme, dans la région ARA et le nombre de garçons nés en 2021 dans la région ARA

Le code suivant permet de savoir si "un département" est dans une liste : 
```python
        listeDeptARA = ["01", "03", "07", "15", "26", "38", "42", "43", "63", "69", "73", "74"]
        Doubs = "25" in listeDeptARA
        # Doubs vaut False
        Isère = "38" in listeDeptARA
        # Isère vaut True
``` 
### 10. En vous aidant de cela, faites une boucle pour compter les naissances dans la Drôme, dans la région ARA et le nombre de garçons nés en 2021 dans la région ARA. Notez les résultats sur votre feuille.
### 11. Calculez le pourcentage de garçons nés dans la région ARA en 2021 par rapport au total des naissances dans la région ARA en 2021. Est-ce cohérent avec la question  
