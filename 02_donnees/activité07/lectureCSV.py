import csv

def recommencerLectureDonnees(fichierCSV, data):
    fichierCSV.seek(0)  # pour considerer toutes les données
    next(data)  # pour éviter les titres


if __name__ == '__main__':
    # lecture des données dans le fichier FD_NAIS_2021.csv
    fichierSource = open('FD_NAIS_2021.csv', mode='r')
    donnees = csv.reader(fichierSource, delimiter=';')

    # le code est à écrire ici





    #dernière ligne du programme : refermer le fichier
    fichierSource.close()