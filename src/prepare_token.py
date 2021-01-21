import json

# entrée: un mot avec une apostrophe | ie. "l'article"
# sortie: deux mots séparés par l'apostrope | ie. "l'" et "article"
def split_apostrophe(word):
    for i, char in enumerate(word):
        if char == "'":
            return word[: i + 1], word[i + 1 :]
    print("oops")
    return 1


# Entrée: arrete sous format json
# Sortie: arrete sous format .txt séparé en entité nommé pour AllenNLP
def prepare_tokens(arrete):

    f = open(
        r"data/tokens/" + arrete["title"][0]["text"][0:17] + ".txt",
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
                        if word[: len(word) - 1] != "":
                            result += word[: len(word) - 1] + " " + "O" + "\n"
                        if word[len(word) - 1 :] != "":
                            result += word[len(word) - 1 :] + " " + "O" + "\n"
                        flag_line = False
                        if word[len(word) - 1] == ".":
                            result += "\n"
                            flag_line = True
                    else:
                        flag_line = False
                        if word != "":
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
                            if word[: len(word) - 1] != "":
                                result += word[: len(word) - 1] + " " + "O" + "\n"
                            if word[len(word) - 1 :] != "":
                                result += word[len(word) - 1 :] + " " + "O" + "\n"
                            flag_line = False
                            if word[len(word) - 1] == ".":
                                result += "\n"
                                flag_line = True
                        else:
                            if word != "":
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
                            if word[: len(word) - 1] != "":
                                result += word[: len(word) - 1] + " " + "O" + "\n"
                            if word[len(word) - 1 :] != "":
                                result += word[len(word) - 1 :] + " " + "O" + "\n"
                            flag_line = False
                            if word[len(word) - 1] == ".":
                                result += "\n"
                                flag_line = True
                        else:
                            if word != "":
                                result += word + " " + "O" + "\n"
                            flag_line = False
        if not flag_line:
            result += "\n"

    f.write(result)
    f.close()


with open(r"data/out/terrasses.json") as json_file:
    data = json.load(json_file)

for arrete in data["arretes"]:
    prepare_tokens(arrete)
