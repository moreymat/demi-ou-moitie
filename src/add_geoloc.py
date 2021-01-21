# -*- coding: utf-8 -*-

import json
import urllib
import urllib.request

with open("src/NLP/terrasses.json") as json_file:
    data = json.load(json_file)

liste_adr = []
for d in data["terrasses"]:
    liste_adr.append(d["adresses"])


# traduis l'adresse en coordonnées
listeCoordinates = []
for ad in range(len(liste_adr)):
    if liste_adr[ad] != "":
        adr_array = liste_adr[ad].split(" ")
        url = "https://api-adresse.data.gouv.fr/search/?q="
        for i in range(len(adr_array) - 1):
            ### partie de remplacement des caractères spéciaux, si y en a qui y sont pas les rajouter
            adr_norm = (
                adr_array[i]
                .replace("’", "")
                .replace("è", "e")
                .replace("é", "e")
                .replace("ë", "e")
                .replace("ç", "c")
                .replace("Â", "A")
                .replace("Ê", "E")
                .replace("È", "E")
                .replace("Ë", "E")
                .replace("É", "E")
                .replace("–", "")
            )
            ###
            url += adr_norm + "+"
        url += adr_array[len(adr_array) - 1]
        print(ad)
        # print(url)
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        data1 = response.read()
        values = json.loads(data1)
        for f_i in range(len(values["features"])):
            tab = [
                values["features"][f_i]["geometry"]["coordinates"][1],
                values["features"][f_i]["geometry"]["coordinates"][0],
            ]
        listeCoordinates.append(tab)


for i in range(len(data["terrasses"])):
    data["terrasses"][i]["locs"] = listeCoordinates[i]


# écriture dans le fichier
with open("data/out/geoloc.json", "w") as f:
    json.dump(data, f, indent=4)
