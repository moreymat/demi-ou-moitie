# functions to manipulate the datas

import json

# Parameter: json_path: path to json file
#
# Output: a string representing the data
def extract_text_from_json(json_path):
    with open(json_path) as json_file:
        data = json.load(json_file)

    result = ""

    for arrete in data["arretes"]:

        for line in arrete["title"]:
            for char in line:
                result += char["text"]
            result += " "
        result += "\n"

        for intro in arrete["intros"]:
            for line in intro:
                for char in line:
                    result += char["text"]
                result += " "
            result += "\n"

        for article in arrete["articles"]:
            for line in article:
                for char in line:
                    result += char["text"]
                result += " "
            result += "\n"
        result += "\n"
        result += "\n"
    return result
