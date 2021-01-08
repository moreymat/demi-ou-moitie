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

#entrée: un mot avec une apostrophe | ie. "l'article"
#sortie: deux mots séparés par l'apostrope | ie. "l'" et "article"
def split_apostrophe(word):
    for i, char in enumerate(word):
        if char == "'":
            return word[:i+1], word[i+1:]
    print("oops")
    return 1

#Entrée: arrete sous format json
#Sortie: arrete sous format .txt séparé en entité nommé pour AllenNLP
def prepare_tokens(arrete):

    f = open(
        r"data/test/" + arrete["title"][0]["text"][0:17] + ".txt",
        "w",
        encoding="utf-8",
    )

    flag_line = False

    result = ""
    for line in arrete["title"]:
        words = line["text"].split(" ")
        for word in words:

            todo = []
            if "'" in word:
                word1, word2 = split_apostrophe(word)
                todo.append(word1)
                todo.append(word2)
            else:
                todo.append(word)
            for word in todo:
                if len(word) > 0:
                    if (
                        word[len(word) - 1] == ","
                        or (word[len(word) - 1] == "." and word[len(word) - 2] != "L")
                        or word[len(word) - 1] == "?"
                        or word[len(word) - 1] == "!"
                    ):
                        result += word[: len(word) - 1] + " " + "O" + "\n"
                        result += word[len(word) - 1 :] + " " + "O" + "\n"
                        flag_line = False
                        if word[len(word) - 1] == ".":
                            result += "\n"
                            flag_line = True
                    else:
                        flag_line = False
                        result += word + " " + "O" + "\n"

    if not flag_line:
        result += "\n"

    flag_line = False
    for intro in arrete["intros"]:
        for line in intro:
            words = line["text"].split(" ")
            for word in words:
                todo = []
                if "'" in word:
                    word1, word2 = split_apostrophe(word)
                    todo.append(word1)
                    todo.append(word2)
                else:
                    todo.append(word)
                for word in todo:
                    if len(word) > 0:
                        if (
                            word[len(word) - 1] == ","
                            or (
                                word[len(word) - 1] == "."
                                and word[len(word) - 2] != "L"
                            )
                            or word[len(word) - 1] == "?"
                            or word[len(word) - 1] == "!"
                        ):
                            result += word[: len(word) - 1] + " " + "O" + "\n"
                            result += word[len(word) - 1 :] + " " + "O" + "\n"
                            flag_line = False
                            if word[len(word) - 1] == ".":
                                result += "\n"
                                flag_line = True
                        else:
                            result += word + " " + "O" + "\n"
                            flag_line = False
        if not flag_line:
            result += "\n"

    flag_line = False
    for article in arrete["articles"]:
        for line in article:
            words = line["text"].split(" ")
            for word in words:
                todo = []
                if "'" in word:
                    word1, word2 = split_apostrophe(word)
                    todo.append(word1)
                    todo.append(word2)
                else:
                    todo.append(word)
                for word in todo:
                    if len(word) > 0:
                        if (
                            word[len(word) - 1] == ","
                            or (
                                word[len(word) - 1] == "."
                                and word[len(word) - 2] != "L"
                            )
                            or word[len(word) - 1] == "?"
                            or word[len(word) - 1] == "!"
                        ):
                            result += word[: len(word) - 1] + " " + "O" + "\n"
                            result += word[len(word) - 1 :] + " " + "O" + "\n"
                            flag_line = False
                            if word[len(word) - 1] == ".":
                                result += "\n"
                                flag_line = True
                        else:
                            result += word + " " + "O" + "\n"
                            flag_line = False
        if not flag_line:
            result += "\n"

    f.write(result)
    f.close()


"""
result = extract_text_from_json(r"data/out/raa_ndeg590.json")

f = open("text.txt", "w", encoding="utf-8")
f.write(result)
f.close()"""

"""fuse_json("data/out/")"""

"""extract_text_from_all_json(r"data/out/all_data.json")"""
