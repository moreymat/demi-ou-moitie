import pdfplumber
import io
import re
import os
from pathlib import Path
import numpy as np
import timeit
import json

# Parameter: table: 2D array
#
# Output: True if table is empty
#        False if not
def table_is_empty(table):
    for line in table:
        for word in line:
            if word != "":
                return False
    return True


# Parameter: page: page from a pdf
#
# Output: True if the page has column
#        False if the page does not have column
def page_has_column(page):

    height = page.height
    width = page.width

    setting_left = {
        "vertical_strategy": "explicit",
        "horizontal_strategy": "explicit",
        "explicit_vertical_lines": [height, width / 6, height, width / 5],
        "explicit_horizontal_lines": [100, width, height - 50, width],
    }

    setting_middle = {
        "vertical_strategy": "explicit",
        "horizontal_strategy": "explicit",
        "explicit_vertical_lines": [height, width / 2 - 8, height, width / 2 + 8],
        "explicit_horizontal_lines": [125, width, height - 50, width],
    }

    table_middle = page.extract_table(setting_middle)
    table_left = page.extract_table(setting_left)
    if table_is_empty(table_middle) and not table_is_empty(table_left):
        return True
    else:
        print("Remove page n°", page.page_number)
        return False


# Parameter: fontstyle from a character
#
# Output: true is the font is bold
#         false if not
def is_bold(fontstyle):
    r = re.compile(".*bold.*")
    if re.match(r, fontstyle.lower()):
        return True
    else:
        return False


def clean_char_metadata(char):
    new_char = {
        "text": char["text"],
        "fontstyle": char["fontname"],
        "size": float(char["size"]),
    }
    return new_char


# Parameter: a pdf
#
# Ouput: pdf content splitted by its column, and cleaned of anything not needed
def pdf_cleaner(pdf):

    clean_pdf = []
    for page in pdf.pages:
        crop = page.crop((0, 50, page.width, page.height))
        if page_has_column(crop):
            current_page = []
            left_column = []
            right_column = []
            left_line = []
            right_line = []
            old_y = crop.chars[0]["y0"]
            old_char = crop.chars[0]["text"]
            for char in crop.chars:
                if not (old_char == " " and char["text"] == " "):
                    old_char = char["text"]
                    if char["x0"] < crop.width / 2:
                        if char["y0"] == old_y:
                            left_line.append(clean_char_metadata(char))
                        else:
                            old_y = char["y0"]
                            left_column.append(left_line)
                            left_line = []
                            left_line.append(clean_char_metadata(char))

                    else:
                        if char["y0"] == old_y:
                            right_line.append(clean_char_metadata(char))
                        else:
                            old_y = char["y0"]
                            right_column.append(right_line)
                            right_line = []
                            right_line.append(clean_char_metadata(char))
            current_page.append(left_column)
            current_page.append(right_column)
            clean_pdf.append(current_page)
    return clean_pdf
    print("done")


# check if both character have same metadatas
def is_same_metadata(c, c2):
    if c["fontstyle"] == c2["fontstyle"] and c["size"] == c2["size"]:
        return True
    else:
        return False


# return a space char with same metadata as c
def get_space_char(c):
    space_char = {"text": " ", "fontstyle": c["fontstyle"], "size": c["size"]}
    return space_char


def clean_line(line):
    new_line = []
    i = 0

    while i < len(line) and not line[i]["text"].isdigit():
        new_line.append(line[i])
        i += 1
    while i < len(line) and line[i]["text"].isdigit():
        new_line.append(line[i])
        i += 1
    if i < len(line) and line[i]["text"] != " ":
        new_line.append(get_space_char(line[i]))

    while i < len(line):
        new_line.append(line[i])
        i += 1

    return new_line


# compress metadatas for a section of an arrété
def compress(line_list):
    compressed = []
    current_string = {}
    current_string["text"] = ""
    current_string["fontstyle"] = line_list[0][0]["fontstyle"]
    current_string["size"] = line_list[0][0]["size"]
    for line in line_list:
        for c in line:
            if is_same_metadata(current_string, c):
                current_string["text"] += c["text"]
            else:
                compressed.append(current_string.copy())
                current_string["text"] = c["text"]
                current_string["fontstyle"] = c["fontstyle"]
                current_string["size"] = c["size"]
        if current_string["text"][len(current_string["text"]) - 1] != " ":
            current_string["text"] += " "
    if len(current_string["text"]) > 0:
        compressed.append(current_string)
    return compressed


# Parameter: clean_pdf: A pdf that went through cleaning
#
# Output: A dictionnary
def get_data_from_clean_pdf(clean_pdf):

    regex_arrete = re.compile("^N° *[0-9]+_+[0-9]+|^[0-9]+/[0-9]+ *– *")
    regex_article = re.compile(
        "^article *[0-9]* +|^Article *[0-9]* +|^ARTICLE *[0-9]* +"
    )
    regex_intro = re.compile("^vu +|^considérant")
    regex_admin = re.compile("^ *DIRECTION|^ *MAIRIES|^ *DELEGATION|^ *Mairie")

    data = {}
    data["arretes"] = []
    current_arrete = {}

    current_title = []
    current_intro_list = []
    current_intro = []
    current_article_list = []
    current_article = []
    current_admin = ""
    current_big_admin = ""

    title_flag = True
    intro_flag = False
    article_flag = False
    big_administration_flag = False
    administration_flag = False

    for page in clean_pdf:
        for column in page:
            for line in column:
                if len(line) > 0 and line[0]["size"] < 10:
                    administration_flag = False
                    big_administration_flag = False
                    string = ""
                    for c in line:
                        string += c["text"]
                    if title_flag:
                        if re.match(regex_intro, string.lower()):
                            title_flag = False
                            intro_flag = True

                            current_arrete["admin1"] = current_big_admin
                            current_arrete["admin2"] = current_admin
                            current_arrete["title"] = compress(current_title)
                            current_title = []
                            current_intro.append(line)
                        else:
                            if len(line) > 0:
                                current_title.append(line)
                    else:
                        if intro_flag:
                            if re.match(regex_intro, string.lower()):
                                current_intro_list.append(compress(current_intro))
                                current_intro = []
                                current_intro.append(line)
                            else:
                                if re.match(regex_article, string.lower()) and is_bold(
                                    line[0]["fontstyle"]
                                ):
                                    intro_flag = False
                                    article_flag = True
                                    current_intro_list.append(compress(current_intro))
                                    current_intro = []
                                    current_arrete["intros"] = current_intro_list
                                    current_intro_list = []
                                    line = clean_line(line)
                                    current_article.append(line)
                                else:
                                    current_intro.append(line)
                        else:
                            if article_flag:
                                if re.match(regex_article, string.lower()) and is_bold(
                                    line[0]["fontstyle"]
                                ):
                                    current_article_list.append(
                                        compress(current_article)
                                    )
                                    current_article = []
                                    line = clean_line(line)
                                    current_article.append(line)
                                else:
                                    if re.match(regex_arrete, string) and is_bold(
                                        line[0]["fontstyle"]
                                    ):
                                        article_flag = False
                                        title_flag = True
                                        current_article_list.append(
                                            compress(current_article)
                                        )
                                        current_article = []
                                        current_arrete[
                                            "articles"
                                        ] = current_article_list
                                        current_article_list = []
                                        data["arretes"].append(current_arrete)
                                        current_arrete = {}
                                        current_title.append(line)
                                    else:
                                        current_article.append(line)
                elif len(line) > 0 and line[0]["size"] >= 10:

                    string = ""
                    for c in line:
                        string += c["text"]

                    if re.match(regex_admin, string):
                        if is_bold(line[0]["fontstyle"]):
                            if big_administration_flag:
                                if current_big_admin[len(current_big_admin) - 1] != " ":
                                    current_big_admin += " "
                                current_big_admin += string
                            else:
                                current_admin = ""
                                big_administration_flag = True
                                current_big_admin = string
                        else:
                            if administration_flag:
                                if current_admin[len(current_admin) - 1] != " ":
                                    current_admin += " "
                                current_admin += string
                                big_administration_flag = False
                            else:
                                administration_flag = True
                                big_administration_flag = False
                                current_admin = string
                    else:
                        if big_administration_flag:
                            if current_big_admin[len(current_big_admin) - 1] != " ":
                                current_big_admin += " "
                            current_big_admin += string
                        elif administration_flag:
                            if current_admin[len(current_admin) - 1] != " ":
                                current_admin += " "
                            current_admin += string

    current_article_list.append(compress(current_article))
    current_arrete["articles"] = current_article_list
    data["arretes"].append(current_arrete)
    return data


start = timeit.default_timer()

data_path = Path("data/raw/")
reps = os.listdir(data_path)

for path in reps:

    pdf_path = data_path / path

    pdf = pdfplumber.open(pdf_path)

    pdf_name = os.path.splitext(path)[0]
    print("Working on", pdf_name, "...")

    clean_pdf = pdf_cleaner(pdf)
    data = get_data_from_clean_pdf(clean_pdf)

    with open(r"data/out/" + pdf_name + r".json", "w", encoding="utf-8") as outfile:
        json.dump(data, outfile)

    print("done")

stop = timeit.default_timer()

print("Run Time: ", stop - start)
