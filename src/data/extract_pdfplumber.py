import pdfplumber
import io
import re
import os
from pathlib import Path
import numpy as np
import timeit

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


def is_bold(fontname):
    r = re.compile(".*bold.*")
    if re.match(r, fontname.lower()):
        return True
    else:
        return False


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
            for char in crop.chars:
                if char["x0"] < crop.width / 2:
                    if char["size"] <= 10:
                        if char["y0"] == old_y:
                            left_line.append(char)
                        else:
                            old_y = char["y0"]
                            left_column.append(left_line)
                            left_line = []
                            left_line.append(char)
                else:
                    if char["size"] <= 10:
                        if char["y0"] == old_y:
                            right_line.append(char)
                        else:
                            old_y = char["y0"]
                            right_column.append(right_line)
                            right_line = []
                            right_line.append(char)
            current_page.append(left_column)
            current_page.append(right_column)
            clean_pdf.append(current_page)
    return clean_pdf
    print("done")


def get_arrete_from_clean_pdf(clean_pdf):

    regex_arrete = re.compile("^N° *[0-9]+_+[0-9]+_VDM|^[0-9]+/[0-9]+ *– *")
    regex_article = re.compile("^article *[0-9]* +|^Article *[0-9]* +|^ARTICLE *[0-9]* +")
    regex_intro = re.compile("^vu +|^considérant")

    arretes = []
    current_arrete = []
    current_title = []
    current_intro_list = []
    current_intro = []
    current_article_list = []
    current_article = []

    title_flag = True
    intro_flag = False
    article_flag = False

    for page in clean_pdf:
        for column in page:
            for line in column:
                string = ""
                for c in line:
                    string += c["text"]
                if title_flag:
                    if re.match(regex_intro, string.lower()):
                        title_flag = False
                        intro_flag = True
                        current_arrete.append(current_title)
                        current_title = []
                        current_intro.append(line)
                    else:
                        current_title.append(line)
                else:
                    if intro_flag:
                        if re.match(regex_intro, string.lower()):
                            current_intro_list.append(current_intro)
                            current_intro = []
                            current_intro.append(line)
                        else:
                            if re.match(regex_article, string.lower()) and is_bold(
                                line[0]["fontname"]
                            ):
                                intro_flag = False
                                article_flag = True
                                current_intro_list.append(current_intro)
                                current_intro = []
                                current_arrete.append(current_intro_list)
                                current_intro_list = []
                                current_article.append(line)
                            else:
                                current_intro.append(line)
                    else:
                        if article_flag:
                            if re.match(regex_article, string.lower()) and is_bold(
                                line[0]["fontname"]
                            ):
                                current_article_list.append(current_article)
                                current_article = []
                                current_article.append(line)
                            else:
                                if re.match(regex_arrete, string) and is_bold(
                                    line[0]["fontname"]
                                ):
                                    article_flag = False
                                    title_flag = True
                                    current_article_list.append(current_article)
                                    current_article = []
                                    current_arrete.append(current_article_list)
                                    current_article_list = []
                                    arretes.append(current_arrete)
                                    current_arrete = []
                                    current_title.append(line)
                                else:
                                    current_article.append(line)

    current_article_list.append(current_article)
    current_article = []
    current_arrete.append(current_article_list)
    current_article_list = []
    arretes.append(current_arrete)
    current_arrete = []
    return arretes


start = timeit.default_timer()

pdf = pdfplumber.open(
    r"C:\Users\Anthony\Downloads\demi-ou-moitie-main\data\raw\raa_610.pdf"
)

clean_pdf = pdf_cleaner(pdf)
arretes = get_arrete_from_clean_pdf(clean_pdf)

result = ""

for arrete in arretes:
    titles = arrete[0]
    intros = arrete[1]
    articles = arrete[2]
    for line in titles:
        for char in line:
            result += char["text"]
        result += " "
    result += "\n"
    for intro in intros:
        for line in intro:
            for char in line:
                result += char["text"]
            result += " "
        result += "\n"
    for article in articles:
        for line in article:
            for char in line:
                result += char["text"]
            result += " "
        result += "\n"
    result += "\n"
    result += "\n"

output = io.open(
    r"data/out/" + r"raa_610" + r".txt", "w", encoding="utf-8"
)  # Ecrit dans le fichier output
output.write(result)
output.close()

stop = timeit.default_timer()

print("Run Time: ", stop - start)
