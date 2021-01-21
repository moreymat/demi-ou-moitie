import json
import difflib  # debugging
import numpy as np
import sys
from utils import sirene_request as sr
from utils import labels as lbl
import os
dir_path = os.getcwd() + "/"


"""
    the purpose of this function is to read a prediction output, collect the dected NE and output them in a json 
    input : predictions with [TOKEN LABEL]
    output : json file
"""
data = {
    "location": [],
    "person": [],
    "organisation": [],
    "date": [],
    "article": [],
    "account": [],
    "application": [],
    "height": [],
    "width": [],
    "surface": [],
}

input_path =  dir_path+"data/predictions/" + sys.argv[1]

def reader(filename):
    f = open(filename, "r")  # reading the predictions
    i = 0
    lines = f.readlines()
    while i < len(lines):  # read all the lines
        line = lines[i].split(
            " "
        )  # splitting by space since we have predictions with the TOKEN[SPACE]LABEL shape
        temp = ""
        if (
            line[1].strip() in lbl.labels
        ):  # if the predicted LABEL is a label and not just an O, we (in theory) are reading a named entity
            current_label = line[1].strip()
            while True:
                temp = temp + line[0] + " "
                if i + 1 >= len(lines):  # if we are out of bounds
                    break
                else:
                    i = i + 1  # moving on to the next word
                line = lines[i].split(" ")
                if (
                    line[1].strip() != current_label
                ):  # if we're outside of the label, we break out of the loop because the entity is most likely ended (unless there is an NER problem)
                    break
            lbl.add_entity(temp, current_label, data)
        i = i + 1


# function to add to JSON
def write_json(data, filename="terrasses.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


with open("terrasses.json") as json_file:
    reader(input_path)
    liste_terrasses = json.load(json_file)
    temp = liste_terrasses["terrasses"]
    reponse = sr.sirene_request(lbl.get_organisation(data))

    y = {
        "type": "terrasse",
        "societe": lbl.get_organisation(data),
        "adresses": lbl.get_location(data),
        "date": lbl.get_date(data),
        "facade": lbl.get_height(data),
        "largeur": lbl.get_width(data),
        "superficie": lbl.get_surface(data),
        "SIREN": sr.get_siren_number(reponse),
        "date_creation": sr.get_creation_date(reponse),
        "nom_arrete": sys.argv[1].split(".")[0],
    }
    temp.append(y)

write_json(liste_terrasses)

"""
reader(input_path)
print(json.dumps(data, indent=4))
# print(data["location"][5].lower() == data["location"][7].lower())
print(lbl.get_location(data))
print("\n")
print(lbl.get_organisation(data))
print("\n")
print(lbl.get_names(data))
print("\n")
print(lbl.get_application(data))
print("\n")
print(lbl.get_width(data))
print("\n")
print(lbl.get_height(data))
print("\n")
print(lbl.get_surface(data))
print("\n")
print(lbl.get_date(data))
print("\n")
"""
