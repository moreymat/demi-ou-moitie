# functions to manipulate the datas

import json
import io
import os
from pathlib import Path
import json

# Parameter: json_path: path to json file
#
# Output: a string representing the data
def extract_text_from_json(json_path):

    with open(json_path) as json_file:
        data = json.load(json_file)

    result = ""

    print("Nombre d'arrété dans ", json_path, ": ", len(data["arretes"]))

    for arrete in data["arretes"]:

        for line in arrete["title"]:
            result += line["text"]
        result += "\n"

        for intro in arrete["intros"]:
            for line in intro:
                result += line["text"]
            result += "\n"

        for article in arrete["articles"]:
            for line in article:
                result += line["text"]
            result += "\n"
        result += "\n"
        result += "\n"
    return result


#Fuse all the json into one
def fuse_json(repertory_path):
    data_path = Path(repertory_path)
    reps = os.listdir(data_path)

    all_datas = {}
    json_list = []

    for json_file in reps:

        datas = {}

        json_path = data_path / json_file

        with open(json_path) as json_file:
            data = json.load(json_file)

        json_name = os.path.splitext(json_path)[0]
        print("Working on", json_name, "...")
        datas["pdf"] = json_name
        datas["content"] = data
        json_list.append(datas)


    all_datas["data"] = json_list

    with open(r"data/out/all_data.json", "w", encoding="utf-8") as outfile:
        json.dump(all_datas, outfile)


#extract text from the fused json
def extract_text_from_all_json(json_path):

    with open(json_path) as json_file:
        data = json.load(json_file)

    result = ""

    nb_arr = 0

    for js in data["data"]:
        print("currently on", js["pdf"])
        for arrete in js["content"]["arretes"]:
            nb_arr += 1
            for line in arrete["title"]:
                result += line["text"]
            result += "\n"

            for intro in arrete["intros"]:
                for line in intro:
                    result += line["text"]
                result += "\n"

            for article in arrete["articles"]:
                for line in article:
                    result += line["text"]
                result += "\n"
            result += "\n"
            result += "\n"
    print("Nombre d'arrété dans ", json_path, ": ", nb_arr)
    return result

"""
result = extract_text_from_json(r"data/out/raa_ndeg590.json")

f = open("text.txt", "w", encoding="utf-8")
f.write(result)
f.close()"""

"""fuse_json("data/out/")"""

"""extract_text_from_all_json(r"data/out/all_data.json")"""
