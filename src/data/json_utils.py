# functions to manipulate the datas

import json
import io

# Parameter: json_path: path to json file
#
# Output: a string representing the data
def extract_text_from_json(json_path):
    with open(json_path) as json_file:
        data = json.load(json_file)

    result = ""

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
