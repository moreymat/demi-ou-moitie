"""Create a dataset from PDF files."""

import pdfplumber
import io
import re
import numpy as np
import timeit


#Parameter: pdf: a pdf
#           font_size: int
#
#Output: pdf with any character with a font size > font_size removed
def remove_big_font_char (pdf, font_size):
    for page in pdf.pages:
        for char in page.chars:
            if(char["size"] > font_size):
                char["text"] = ""
    return pdf



#Parameter: table: 2D array
#
#Output: True if table is empty
#        False if not
def table_is_empty(table):
    for line in table:
        for word in line:
            if word != "":
                return False
    return True


    

#Parameter: page: page from a pdf
#
#Output: True if the page is empty
#        False if the page is not
def page_is_empty(page):

    setting = {
        "vertical_strategy": "text",                
        "horizontal_strategy": "text",                 
    }

    table = page.extract_table(setting)
    if table is None:
        print("Remove page n°", page.page_number)
        return True
    else:
        return False




#Parameter: page: page from a pdf
#
#Output: True if the page has column
#        False if the page does not have column
def page_has_column(page):

    setting = {
        "vertical_strategy": "explicit",         
        "horizontal_strategy": "explicit",          
        "explicit_vertical_lines": [height, width/2-15, height, width/2+15],
        "explicit_horizontal_lines": [100, width, height-50, width],
    }

    table = page.extract_table(setting)
    if(table_is_empty(table) and not page_is_empty(page)):
        return True
    else:
        print("Remove page n°", page.page_number)
        return False


#Parameter: pdf: a pdf
#           setting: settings for the extract table function (see doc)
#Output: a texte file with arrêté splitted
def split_arrete(pdf, setting):
    print("cleaning...")
    clean_start = timeit.default_timer()
    pdf = remove_big_font_char(pdf, 10)
    clean_stop = timeit.default_timer()
    print("pdf cleaned in ", clean_stop - clean_start)

    height = pdf.pages[0].height
    width = pdf.pages[0].width

    result = ""

    previous_line_empty = False
    for page in pdf.pages:
        crop = page.crop((0, 50, page.width, page.height))
        if page_has_column(crop):
            table = crop.extract_table(setting)
            array = np.array(table)
            for column in range(2):
                for line in array[:,column]:             #Renvoie un tableau de charactère
                    if len(line) > 0:                  #Si la string n'est pas vide  
                        
                        temp = np.array2string(line)       #Renvoie un string de la forme <'string'>                  
                        string = temp[1:len(temp)-1]
                        
                        regex = re.compile('^[0-9]*/[0-9]* *– *')
                        regex1 = re.compile('^N° *[0-9]*_*[0-9]*_VDM *[A-Z]')
                        regex2 = re.compile('^article [0-9]*  |^vu ')
                        if (previous_line_empty and string.startswith("N° ")) or re.match(regex, string) or re.match(regex1, string):      #Detecte les arretés
                            result += "\n\n\n\n"
                        else:                      
                            if (previous_line_empty and string.lower().startswith("article ")) or re.match(regex2, string.lower()):       #Detecte les différentes parties de l'arreté
                                result += "\n"

                        result +=  string + " "
                        previous_line_empty = False
                    else:
                        previous_line_empty = True
                        

                    
                        

    output = io.open(r"data\text\out.txt", "w", encoding="utf-8")
    output.write(result)
    output.close()


pdf = pdfplumber.open(r"C:\Users\Anthony\Downloads\demi-ou-moitie-main\data\raw\raa_610.pdf")

height = pdf.pages[0].height
width = pdf.pages[0].width

ys = []
for y in range(0, int(height), 7):
    ys.append(int(width))
    ys.append(y)

setting = {
        "vertical_strategy": "explicit",                    #Explicit: je définis les lignes de séparations
        "horizontal_strategy": "explicit",                      #Text: Les lignes de textes définissent les séparations
        "explicit_vertical_lines": [height, 30, height, width/2, height, width-30],     #Ligne explicit: A gauche, au mileu, a droite pour séparat les colonnes
        "explicit_horizontal_lines": ys,
    }


start = timeit.default_timer()

split_arrete(pdf, setting)

stop = timeit.default_timer()
print('Run Time: ', stop - start) 
