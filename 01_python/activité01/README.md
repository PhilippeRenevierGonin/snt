# SNT, Activité 01 : découverte de Python

## 1. code initial
Pour cette première activité, récupérez (téléchargement ou en copier coller) : [le code python initial (fichier 01_carte.py)](01_carte.py) 

Pour cela : ouvrez Thonny et dans ce logiciel, ouvrez le fichier téléchargé ou copier le code dans un nouveau fichier.
Quand vous modifiez le fichier, pensez à sauvegarder (CTRL+S ou le bouton ![save.png](../../images/save.png))

Exécutez ce script en utilisant "Déboguer le script courant", c'est le bouton avec l'image ![deboguer.png](../../images/deboguer.png). Puis utilisez "entrez dans l'étape en cours (F7)" ![F7.png](../../images/F7.png), ceci permet de voir le dérouler du script.

Répondons collectivement aux questions suivantes, en prenant note des réponses. 

### 1.1 Est-ce qu'une ligne commençant par "#" est-elle prise en compte ? 


### 1.2 Quel est le role de "rue", "codepostal", "ville" ?
```python
    rue = "32 Barthelemy De Laffemas"
    codepostal = "26000"
    ville = "Valence"
```

### 1.3 Quel est le rôle de "url" ? est-ce différent ?

Notez bien le nom que prend le "+" et dans quel cas il fonctionne. 


### 1.4 Qu'est-ce que "requests" ? Difficile de répondre à cette question. Alors décomposons cette question : 

 - Notez les lignes où "requests" apparait 
```python
import requests
# [...]
    headers = requests.utils.default_headers()
# [...]    
    reponse = requests.get(url, headers=headers)
```
 - c'est en anglais, mais qu'est-ce que cela peut vouloir dire ?
 - rechercher "requests python" dans un moteur de recherche

### 1.5 Identifiez deux instructions conditionnelles 

Combien il y a de cas possibles ? 
Modifiez le script pour couvrir tous les cas :
 - exécutez le script avec les valeurs initiales
 - modifiez le nom de la ville par une ville inexistante (pas de réponse) : "Aucune donnée trouvée."
 - changez url  par ```url = "https://nominatim.openstreetmap.org/unepage"```
Remettez le code avec les valeurs initiales

### 1.6 Qu'est-ce que "donnees" dans ce code ? 

Allez sur le site [https://jsonviewer.io](https://jsonviewer.io/) pour y coller la 2e ligne qui est affichée suite à l'exécution du script. Ensuite, visualisez et explorez les données.  

### 1.7 complétons un peu le code 
Faites en sorte d'afficher les valeurs (dans cet ordre) de lat (pour latitude) et de lon (pour longitude). Pour y arriver, utilisez la fonction "print", comme lorsque 
Allez sur google.com/maps et coller ces deux valeurs (la latitude puis la longitude). 

## 2. Bilan

Notons les notions, et assicions les éléments vus correspondant à ces notions, tout d'abord sur les éléments de python : 
 - variables
 - concaténation de chaines de caractères
 - module
 - insctuction conditionnelle

Maintenant sur des éléments liés aux thèmes que nous verrons dans SNT : 
 - adresse d'une page web (url)
 - service disponible sur le web
 - format de données "json"
 - cartographie 

