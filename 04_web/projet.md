# Projet web

Par groupe (demie-classe), nous allons construire un site web. Voici le déroulé :
1. vous allez construire le contenu de page pour un rendu fin mars
2. vous réaliserez des pages web grâce aux contenus début avril
3. vous organiserez le site web en regroupant les pages en mai
4. vous créerez la navigation entre les pages en mai

## 1. Élaborer le contenu des pages

Le contenu des pages doit être une thématique liées aux chapitres 4 (localisation cartographie, mobilité), 5 (photographie numérique), 6 (réseaux sociaux) ou 7 (informatique embarquée) du amnuel "SNT, édition Delagrave". 
À partir des informations comprises dans le manuel, vous compléterez en recherchant des informations complémentaires ou vous réaliserez des illustrations. 

Vous ferez valider votre ou vos thématiques auprès de votre enseignant. 

Vous devrez citer vos sources, en faisant attention aux droits sur les images, et si vous utilisez des outils IA, identifiez clairement les passages concernés. 

La taille de ce contenu doit faire 2000 caractères minimum (espace compris), 3000 maximum. 

Il n'y a pas de mise en forme attendue à ce stade, cela sera fait en html/css. 

Il faut une page par élève, mais vous pourrez vous mettre en groupe pour faire les pages (1 élève seul·e fait une page, deux élèves en font deux, trois en font trois, etc.).

Les modalités de rendu seront préciser en classe (via "Echange")

## 2. Réalisation des pages web
à faire en séance à partir du contenu préparé. 


## 3. Organisation du site et 3. Navigation

Réfléchissez au regroupement de pages en différentes catégories. Modifiez le fichier "plan.html" contenant les liens vers toutes les pages pour refléter vos catégories. Pour chaque catégorie, il doit y avoir une div selon le modèle : 
```html
<nav>
        <div><span>titre de la catégorie</span>
            <ul>
                <li><a href="xxx">page de la catégorie</a></li>
                <li><a href="xxx">page de la catégorie</a></li>
                <!-- ... suite des liens pour cette catégorie -->
            </ul>
        </div>
        <div><span>titre d'uen autre catégorie</span>
            <ul>
                <li><a href="xxx">page de cette catégorie</a></li>
                <li><a href="xxx">page de cette catégorie</a></li>
                <!-- ... suite des liens pour cette catégorie -->
            </ul>
        </div>
        <!-- ... suite des catégories -->
    </nav>
```

Pour la navigation entre page, optez pour un des solutions suivantes : 
 - insérez ce plan dans toutes les pages
 - insérez un lien "page précédente" et un lien "page suivante" dans chaque page
 - ou les deux

Après avoir inséré le plan dans une des pages, essayez [le fichier css](menu.css). 

Réfléchissez sur des moyens de mettre en valeur la page "actuelle" ?
