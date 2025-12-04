# pseudocode:
import json


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

def calculer_translation(dict_coord, dict_trans):
    dict_nouveau = {}
    try:
        for forme, value in dict_coord.items():
            #print(forme)
            dict_nouveau[forme] = []
            for sommet in value:
                ls_sommet = sommet.split(',')
                x = int(ls_sommet[0]) + int(dict_trans[forme][0])
                y = int(ls_sommet[1]) + int(dict_trans[forme][1])
                #print(x,y)
                dict_nouveau[forme].append(str(x) + "," + str(y))
        return dict_nouveau
    except:
        return None

# def écrire les nouvelles coordonées dans un autre fichier
# créer/ouvrir un fichier texte
    #pour k, v dans nouvelle_coord
        #écrire k , v dans le fichier

def ecrire_translation(nouvelles_coord):
    with open("nouveau.txt", "w") as file:
        for k, v in nouvelles_coord.items():
            file.write(k + ' ' + " ".join(v) + '\n')

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
nouveau_dict = calculer_translation(dict_coord, dict_tans)
print(nouveau_dict)
ecrire_translation(nouveau_dict)