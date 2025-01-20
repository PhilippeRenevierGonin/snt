# Activité 9 : collecte puis exploitation des données avec Excel

En classe, nous allons écouter quelques musiques. Vous aurez à remplir anonymement un questionnaire lié à l'écoute. 
Puis, il faudra "dépouiller" les résultats : en les saisissant dans Excel. Finalement, nous pourrons conclure sur cette expérience. 

## Phase d'écoute
Écoutez les morceaux et remplissez votre formulaire sans mettre de signe distinctif. 

Pour chaque morceau, cochez les cases pour : 
 - indiquer si le style du morceau correspond à vos habitudes d'écoute
 - indiquer si vous appréciez le morceau
 - indiquer sa position (ou non) dans le top 3 de la "playlist" du jour

Une fois les documents remplis, deux d'entre vous rendent à l'enseignant, puis vont ramasser les autres documents.
L'enseignant attribuera une lettre à chaque document, cela permettre de noter dans les fichiers Excel quels documents ont été saisis.

## Préambule
Discutons du déroulement de l'activité et décidons ensemble de la validité (ou non) d'une réponse. 

## Phase de saisie
Par deux, il faut saisir dans 2 fichiers Excel différents, un pour traiter les morceaux préférés et un pour traiter les appréciations / habitudes
 - Pour le groupe du mardi 13h50 : [appreciation-habitude](appreciation-habitude-m1350.xlsx) et [les tops 3](top-m1350.xslx)
 - Pour le groupe du mardi 15h15 : [appreciation-habitude](appreciation-habitude-m1550.xlsx) et [les tops 3](top-m1550.xslx)

Pour saisir en parallèle, nous saisirons par 2 documents puis nous ferons circuler les documents. 

## Phase analyse

Pour remplir, suivez l'exemple de l'enseignant. 

Proposez des vérifications de saisies correctes (soit via une personne, soit via une formule excel). Dans excel, nous pouvons compter (avec de SOMME ou des NB.SI) et vérfier que le compte est bon. 
Nous pouvons aussi utiliser des "SI" pour vérifier qu'une condition est respectée : par exemple il ne peut y avoir que 0 ou 1 "top 1".

### Habitudes d'écoute et Appréciation des morceaux
Pour cette partie, il faudra compter (avec NB.SI) le nombre de morceaux qui ne faisaient pas partie des styles de musiques habituellement écoutés par les personnes ayant répondu. Ces morceaux seront appelés morceaux "hors style". 

Puis, il faudra compter (avec NB.SI.ENS) le nombre de morceaux "hors style" qui ont été appréciés.

Finalement, il faudra déterminer le taux de morceaux "hors style" appréciés par rapport au nombre de morceaux "hors style". 

Proposez d'autres "statistiques" pour mettre en valeur (ou pas) les morceaux "hors style"

Calculez dans Excel : 
- le taux d'appréciation par morceau (nombre de "j'apprécie" sur le nombre de réponses)

Proposez des vérifications de calculs (via des formules excel).


### TOP 3

Calculez dans Excel :
 - déterminer le nombre de top1, top2 et top3 par morceau. Refaites un tableau avec ces totaux. 
 - le classement (par tri) des morceaux en comptant le nombre de fois où il est "top 1". Pour départager (ceci se fait dans les paramètres du tri), regardez le nombre de fois où le morceau est top 2 puis top 3  
 - calculer un score : 3 points pour chaque "top 1", 2 points pour chaque "top 2" et 1 point pour chaque "top 3".  Classez selon ce score. 

Est-ce que les classements sont identiques ? Si l'on attribue 4 points au lieu de 3 pour chaque top 1, est-ce que le classement change ? 