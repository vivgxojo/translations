# pseudocode:

#ouvrir le fichier avec le module csv.reader
    #faire un dictionnaire de listes 2D avec les coordonnées
    #dict_coord[row[0]] = [row[1:3]]
    #faire un dictionnaire de listes pour les translations
    #dict_tans[row[4]] = [row[5]]

# def calculer les translation
    # boucle pour chaque forme
        # boucle pour nb sommet dans la liste
            # x = sommet[0] + dict_trans[forme][0]
            # y = sommet[1] + dict_trans[forme][1]

# def écrire les nouvelles coordonées dans un autre fichier


import csv
dict_coord = {}
dict_tans = {}
with open("objets.txt", "r") as file:
    reader = csv.reader(file, delimiter=" ")
    for row in reader:
        dict_coord[row[0]] = row[1:-2]
        dict_tans[row[0]] = row[-1].split(",")
print(dict_coord)
print(dict_tans)