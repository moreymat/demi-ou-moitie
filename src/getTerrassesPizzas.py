import json
from typing import Dict, List


def contains(arrete, string):
    if string in arrete:
        return True


with open("data/out/all_data.json") as json_file:
    data = json.load(json_file)

terrasses: Dict[str, List[str]] = {"arretes": []}
pizzas: Dict[str, List[str]] = {"arretes": []}

for i in range(len(data["data"])):
    for j in range(len(data["data"][i]["content"]["arretes"])):
        for k in range(len(data["data"][i]["content"]["arretes"][j]["title"])):
            dejaTerrasse = 0
            dejaPizza = 0
            if (
                contains(
                    data["data"][i]["content"]["arretes"][j]["title"][k]["text"],
                    "- Terrasse - ",
                )
                and dejaTerrasse == 0
            ):
                print(
                    "L'arrete "
                    + str(i)
                    + ","
                    + str(j)
                    + ' est de la classe "terrasse" !'
                )
                terrasses["arretes"].append(data["data"][i]["content"]["arretes"][j])
                dejaTerrasse += 1
            if (
                contains(
                    data["data"][i]["content"]["arretes"][j]["title"][k]["text"],
                    "AMBULANTE DE PIZZA",
                )
                and dejaPizza == 0
            ):
                print(
                    "L'arrete "
                    + str(i)
                    + ","
                    + str(j)
                    + ' est de la classe "camion à pizza" !'
                )
                pizzas["arretes"].append(data["data"][i]["content"]["arretes"][j])
                dejaPizza += 1

with open("data/out/terrasses.json", "w") as outfile:
    json.dump(terrasses, outfile)

with open("data/out/pizzas.json", "w") as outfile:
    json.dump(pizzas, outfile)
