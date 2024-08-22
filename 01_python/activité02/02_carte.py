import math
import requests


# point d'entrée du script
if __name__ == '__main__':
    #définitaiton de variables
    rue = "37-39 Barthelemy De Laffemas"   # todo :
    codepostal = "26000"
    ville = "Valence"
    url = "https://nominatim.openstreetmap.org/search?q=" + rue + " " + codepostal + " " + ville + "&format=json" + "&addressdetails=1&polygon_svg=1"
    zoom = 17

    # le script affiche une adresse d'une page de recherche
    print(f"adresse de la page de recherche : {url}")

    # ceci pour faire passer ce script pour un navigateur web, ici firefox
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0'  # Exemple : User-Agent de Firefox
    })

    # on lance la recherche en interrogeant le serveur à distance
    reponse = requests.get(url, headers=headers)

    # si la requête a fonctionné (code réponse 200)
    if reponse.status_code == 200:
        # le script affiche toute la réponse reçue
        print("données reçues : "+reponse.text)
        # le script demande la conversion des données reçues en une liste/tableau
        donnees = reponse.json()

        # s'il y a des données
        if donnees:
            lat = float(donnees[0]['lat']) #conversion d'une valeur "string" à "float"
            lon = float(donnees[0]['lon'])
            print(f"Latitude: {lat}, Longitude: {lon}")

            # conversion latitude, longitude en numéro d'image de OpenStreetMap pour voir la carte
            # ref : https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames
            lat_rad = math.radians(lat)
            n = math.pow(2, zoom)
            xtile = n * ((lon + 180) / 360)
            ytile = n * (1 - (math.log(math.tan(lat_rad) + 1 / math.cos(lat_rad)) / math.pi)) / 2
            # math.floor : pour obtenir un arrondi à l'entier inférieur le plus proche, par exemple 24.12 -> 24 ou 24.75 -> 24
            x = math.floor(xtile)
            y = math.floor(ytile)
            # le script affiche un lien vers une image
            print(f"https://tile.openstreetmap.org/{zoom}/{x}/{y}.png")

            # le script crée ou écrase un fichier "carte.html" (le fichier sera à côté du fichier 02_carte.py)
            pageweb = open("carte.html", "w")
            # le script écrit une page web
            pageweb.write("<!DOCTYPE html>\n")
            pageweb.write("<html lang=\"fr\">\n")
            pageweb.write("<head>\n\t<meta charset=\"UTF-8\">\n\t<title>carte 1x1</title>\n")
            # todo : il faudra faire l'inclusion d'un style CSS
            pageweb.write("</head>\n")
            pageweb.write("<body>\n<div id=\"carte\">\n")
            # todo : ici, il faudra ajouter d'autres images
            pageweb.write(f"\t<img src=\"https://tile.openstreetmap.org/{zoom}/{x}/{y}.png\">\n")
            pageweb.write("</div>\n</body>\n</html>")
            pageweb.close()

        else:
            print("Aucune donnée trouvée.")
    else:
        print("Erreur lors de la requête." + str(reponse.status_code))

