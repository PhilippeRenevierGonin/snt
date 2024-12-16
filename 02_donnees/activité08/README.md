# Activité 8 : manipulation des données avec Excel

Pour cette activité, nous allons utiliser Excel sur le fichier csv. 

Si vous ne l'avez pas conservé, récupérez  [le fichier FD_NAIS_2021.csv des naissances de 2021](../activité07/FD_NAIS_2021.csv) et ouvrez-le avec Excel (si Excel vous demande de convertir les valeurs avec des 0 non-significatifs, dites non).
Faites "enregistrer sous..." (touche F12) pour enregistrer le fichier au format xlsx. Cela permet de conserver les modifications au "format excel"

En parallèle, vous pouvez ouvrir le fichier dans excel et consulter la [définition des variables dans le fichier de référence](https://www.insee.fr/fr/statistiques/fichier/6652024/Contenu_etatcivil2021_nais2021.pdf) : 

**Sur une feuille que vous rendrez à la fin de l'activité, répondez aux questions suivantes.**

## Une première formule dans Excel

### 1. Rappelez ce qu'est un "tableur"

Excel permet de faire des formules, par exemple la moyenne. Pour faire une formule, il faut saisir dans une case la "valeur" suivante : 
 - le premier caractère de la case doit être le symbole "=" 
 - en suite, il est possible de faire une formule : une simple opération mathématique (+,*,...) ou une formule plus complexe avec des fonctions d'Excel.

Où taper les formules : en princpe n'importe où cela ne gêne pas, par exemple, il faut éviter de mettre "au milieu" des données. Il est de coutume de faire des formules sous le tableau.
Comme le fichier est grand, pour conserver la vue de la première ligne, allez dans "Affichage > Figer les volets > Figer la ligne supérieure". Puis descendez "en bas" du fichier (ligne 742053).
En principe, vous voyez encore les titres de la ligne 1. 

sur la ligne 742054, colonne C, tapez :  "=MOYENNE(C2:C742053)" puis validez.

### 2.  Qu'est-ce qui est affiché dans excel, dans la partie tableau ? Qu'est-ce qui est affiché dans la partie "édition de la case" ? Le résultat est-il différent de ce que vous aviez trouvé avec Python ?

Une case dans Excel est aussi appelée aussi cellule. Pour les désigner, il faut utiliser ses "coordonnées" : la colonne suivie de la ligne. 
Par exemple C742054 désigne la cellule de la colonne C qui est ligne 742054. 

Cliquez sur la cellule C742054 puis déplacez la souris en bas à droite de cette case : le curseur doit changer de <img src="curseurCase.png" style="width:1rem;height:1rem"> à <img src="curseurRépliquer.png" style="width:1rem;height:1rem">. Quand c'est le cas, cliquez en laissant le bouton de la souris enfoncé, ensuite déplacer la souris sur la droite. Quand la cellule d'à côté est surlignée (en vert), relachez le bouton de la souris.

### 3. Que contient a cellule D742054 (dites ce qui est affiché et ce qui est dans la partie "édition de case") ? 

Il y a d'autres formules que "MOYENNE", il y a par exemple "MIN et MAX" qui fonctionnent comme "MOYENNE" en prenant une "plage" de valeurs, c'est-à-dire un ensemble de cellules.

Note 1 : cet ensemble pourrait être discontinu (on pourrait le faire à la souris en maintenant le bouton "Ctrl" enfoncé) 

Note 2 : cet ensemble pourrait être aussi sur plusieurs colonnes

Nous ne ferons qu'avec une colonne entière. Ici, prendre en compte tous les âges de mères d'un enfant né en 2021 se note : C2:C742053 avec C2 qui détermine la première cellule et CC742053 la dernière.

### 4. En plaçant des formules Essayez de déterminer l'âge le plus jeune et l'âge le plus vieux notés pour les mères. Retrouvez-vous le même résultat qu'avec Python ? 

### 5. Sommes-nous sûr que ces âges sont les âges rééls ? 

### 6. "Répliquez" ces deux formules pour l'âge des pères sans utiliser ni le clavier ni le copier-coller ni la reconnaissance vocale. Notez comment vous avez fait.    


## Fonctions d'Excel avec plusieurs paramètres

Certaines fonctions d'Excel peuvent prendre plusieurs paramètres. C'est le cas de NB.SI quyi est faite pour compter les cellules pour lesquelles une condition est vraie. Cette condition est appelée critère.

En bas de la colonne L, tapez : "=NB.SI(L2:L742053;"26")".

Le premier paramètre est plage de valeur (ici la colonne L) et le 2e paramètre est le critère qui doit être vérifié. Ici "26" est comme écrire "=26", c'est-à-dire qu'Excel ne va compter que les cellules qui sont égales à "26".  

### 7. Retrouvez-vous le même résultat qu'avec Python ? 

Sachant que : 
 - il existe une fonction "SOMME" dans Excel
 - les départements de la région ARA sont "01", "03", "07", "15", "26", "38", "42", "43", "63", "69", "73", "74"

### 8. Pouvez-vous faire déterminer avec Excel le nombre de naissances dans la région ARA en 2021 ? Décrivez comment vous avez fait. 

La fonction NB.SI.ENS permet de faire un décompte avec plusieurs critères :
 - une première paire plage_critères1 / critère1 qui fonctionne comme avec NB.SI
 - puis il est possible d'ajouter d'autres paires (jusqu'à 127) 
 - toutes les "plages_critères" doivent avoir le même nombre de lignes (et de colonnes)
 - pour que le nombre augmente, il faut que tous les crièteres soient vérifiée

### 9. Déterminez avec Excel le nombre de garçons nés en 2021 dans la région ARA. Notez comment vous avez fait.  


## Faire un graphique

Nous allons voir 2 dernières choses : fixer une plage et faire un graphique. 

Dans une plage de valeurs, par exemple L2:L742053, si on utilise la réplication de la formule comme à la question 3, la plage change : si on décale horizontalement, la colonne change (L deviendra une autre lettre), si on décale verticalement les numéros de ligne (2 et 742053) changeront. 
Pour éviter une modification de la plage de valeurs, il est possible d'ajouter des $ avant le nom de la colonne ou le numéro de la ligne, par exemple en cas de "réplication" : 
 - $L$2:$L$742053 : la plage de valeurs ne peut pas changer
 - $L2:$L742053 : la colonne ne peut pas changer mais les lignes oui
 - L$2:L$742053 : la colonne peut changer mais les lignes non
 - $L$2 : la cellule sera toujours celle de la colonne L, 2e ligne
 - $l2 : la cellule sera toujours de la colonne L mais la ligne peut changer
 - L$2 : la cellule pourra "changer" de la colonne mais elle sera toujours sur la 2e ligne

Un peu plus bas dans le fichier par exemple ligne 742075, mettez "département" dans la colonne A puis 1 dans la colonne B puis dans la cellule d'en-dessous, mettez "nb naissances 2021" dans la colonne A et dans la colonne B la formule qui donne le nombre de naissances dans le département de l'ain (01 ou 1), maius : 
 - en utilisant NB.SI
 - en fixant la plage pour les départements avec les "$" 
 - le critère pour compter doit être la case au-dessus.

Sélectez les deux cases avec la souris et répliquez (quand vous avez le curseur <img src="curseurRépliquer.png" style="width:1rem;height:1rem">) ces deux cases sur plusieurs colonnes (par exemple jusqu'à 32 ou un peu plus, le nombre importe peu tant qu'on ne dépasse pas 95). 

### 10. Qu'obtenez-vous ? Que constatez-vous pour le "20" ? pourquoi ? Réglez le problème pour cette cellule uniquement sachant que vous pouvez faire un "+" entre 2 NB.SI. Notez comment vous avez fait.

Sélectionnez les lignes 742075 et 742076 (en cliquant sur la gauche sur les numéros des lignes). Ensuite, allez dans "Insertion > nuage de points > courbes "

### 11. Visuellement, dans quel département parmi les premiers départements, y a-t-il le plus de naissances ?  Pouvons nous en déduire que c'est dans ce département que la natalité est la plus forte ? Si non, quelle(s) information(s) manqueraient-ils ?

### 12. Est-ce que pour les départements (ou territoires) d'outres mers (971-974 et 976) pourrait sur le même graphique Excel ? Quel serait le problème et la solution ?   

Indication : vous pouvez consulter la page [Téléchargement du fichier d'ensemble des populations légales en 2021 de l'INSEE](https://www.insee.fr/fr/statistiques/7739582?sommaire=7728826#consulter)