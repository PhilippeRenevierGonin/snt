import requests

# point d'entrée du programme
if __name__ == '__main__':
    #définitaiton de variables
    rue = "32 Barthelemy De Laffemas"
    codepostal = "26000"
    ville = "Valence"
    url = "https://nominatim.openstreetmap.org/search?q="+rue + " " + codepostal + " " + ville + "&format=json" + "&addressdetails=1&polygon_svg=1"

    # le programme affiche une adresse d'une page de recherche
    print(f"adresse de la page de recherche : {url}")
    
    # ceci pour faire passer ce programme pour un navigateur web, ici firefox
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0'  # Exemple : User-Agent de Firefox
    })
    
    # on lance la recherche en interrogeant le serveur à distance
    reponse = requests.get(url, headers=headers)
    
    # si la requête a fonctionné (code réponse 200)
    if reponse.status_code == 200:
        # le programme affiche toute la réponse reçue
        print("données reçues : "+reponse.text)
        # le programme demande la conversion des données reçues en une liste/tableau
        donnees = reponse.json()
        
        # s'il y a des données
        if donnees:
            lat = donnees[0]['lat']
            lon = donnees[0]['lon']
            # TODO : ici, affichez avec print lat (en premier) et lon (en second)
        else:
        # s'il n'y a pas de données
            print("Aucune donnée trouvée.")
    else:
    # si la requête n'a pas fonctionné
        print("Erreur lors de la requête."+str(reponse.status_code))