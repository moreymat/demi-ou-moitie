import numpy as np
from difflib import SequenceMatcher
from string import ascii_letters, digits

"""
    List of all the labels we previously created
"""

labels = [
    "I-LOC",  # location
    "I-PER",  # Person
    "I-ORG",  # organisation
    "I-DAT",  # date
    "I-ART",  # article number
    "I-CMP",  # account number
    "I-DMD",  # application number
    "I-SAI",  # dimensions
    "I-LRG",  # dimensions
    "I-SUP",  # dimensions
]
type_societe = [
    "EI",
    "EIRL",
    "EURL",
    "SARL",
    "SA",
    "SAS",
    "SASU",
    "SNC",
    "SCOP",
    "SCA",
    "SCS",
]

#############
#   UTILS   #
#############

"""
    Purpose : checks if a string represents an int
    input : string to be tested
    output : True if string does represent an integer else False
"""


def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# Same thing for floats


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def isAnOrganisation(entity_array):
    for e in entity_array.split(" "):
        if e.upper().strip() in type_societe:
            return True
    return False


#############
# FUNCTIONS #
#############

"""
    purpose : adding named entities to a dict
    input : named entity, 
            named entity predicted label (to know to which array in the dict we're appending it to), 
            the dictionary we're adding it to
    output : none
"""


def add_entity(entity, label, data):
    if label == "I-LOC":
        data["location"].append(entity)
    if label == "I-PER":
        data["person"].append(entity)
    if label == "I-ORG":
        data["organisation"].append(entity)
    if label == "I-DAT":
        data["date"].append(entity)
    if label == "I-ART":
        data["article"].append(entity)
    if label == "I-CMP":
        data["account"].append(entity)
    if label == "I-DMD":
        data["application"].append(entity)
    if label == "I-SAI":
        data["height"].append(entity)
    if label == "I-LRG":
        data["width"].append(entity)
    if label == "I-SUP":
        data["surface"].append(entity)


"""
    purpose : get the right entity out of the all the possible entities recognized, return the one that appears the most
    input : array of entity
    output : correct entity
"""


def get_location(data):
    entity_array = data["location"]
    most_times_equals = 0
    entity = ""
    # simple double loop to find the max occurences
    for i in range(0, len(entity_array)):
        nbr_times_equal = 0
        for j in range(0, len(entity_array)):
            # if they're both the same entities (likely when looking for the adress, we might scrape the relevent one a few times)
            if (
                entity_array[i].lower() == entity_array[j].lower()
                and i != j
                and entity_array[i].strip().lower() != "marseille"
                and len(entity_array[i]) > 15
                and len(entity_array[i].split(" ")) > 5
            ):
                nbr_times_equal = nbr_times_equal + 1
                if nbr_times_equal > most_times_equals:
                    most_times_equals = nbr_times_equal
                    entity = entity_array[i]
    if entity == "" or most_times_equals <= 1:
        return get_location_by_similarity(data)
    else:
        return entity


def get_location_by_similarity(data):
    entity_array = data["location"]
    most_times_equals = 0
    entity = ""
    # simple double loop to find the max occurences
    for i in range(0, len(entity_array)):
        if (
            entity_array[i].strip().lower() != "marseille"
            and len(entity_array[i].split(" ")) > 4
        ):
            for j in range(0, len(entity_array)):
                score = similar(entity_array[i].upper(), entity_array[j].upper())
                if score > 0.85:
                    if len(entity_array[i]) > len(entity_array[j]):
                        entity = entity_array[i]
                    else:
                        entity = entity_array[j]
    if entity == "":
        return "NA"
    else:
        return entity


def get_names(data):
    entity_array = data["person"]
    entity = ""
    # simple double loop to find the max occurences
    for i in range(0, len(entity_array)):
        nbr_times_equal = 0
        if len(entity_array[i].split(" ")) > 1 and len(entity_array[i].split(" ")) < 4:
            if (
                entity_array[i].split(" ")[0].isupper()
                and entity_array[i].split(" ")[0].strip() != "LOTA"
            ):
                try:
                    list(entity_array[i].split(" ")[1])[0].isupper()
                except IndexError:
                    err = 2
                else:
                    entity = entity_array[i]
        elif len(entity_array[i].split(" ")) == 1:
            if (
                entity_array[i].split(" ")[0].isupper()
                and entity_array[i].split(" ")[0].strip() != "LOTA"
                and set(entity_array[i].split(" ")[0].strip()).difference(
                    ascii_letters + digits
                )
                == False
            ):
                er = 2
                # entity = entity_array[i]
    if entity == "":
        return "NA"
    else:
        return entity


def get_organisation(data):
    entity_array = data["organisation"]
    entity = ""
    # simple double loop to find the max occurences
    for i in range(0, len(entity_array)):
        nbr_times_equal = 0
        if isAnOrganisation(entity_array[i]):
            entity = entity_array[i]
    if entity == "":
        return "NA"
    else:
        return entity


def get_application(data):
    entity_array = data["application"]
    for i in range(0, len(entity_array)):
        try:
            first, last = entity_array[i].split("/")
        except ValueError:
            err = 0
        else:
            if isInt(first) and isInt(last):
                return entity_array[i]
    return "NA"


def get_height(data):
    entity_array = data["height"]
    h = ""
    for i in range(0, len(entity_array)):
        try:
            height = entity_array[i].split(" ")
        except ValueError:
            err = 0
        else:
            for j in range(0, len(height)):
                if height[j].strip() == "m" or height[j].strip() == "saillie":
                    try:
                        first, last = height[j].split(",")
                    except ValueError:
                        if isInt(height[j]):
                            h = height[j]
                    else:
                        if isInt(first) and isInt(last):
                            h = height[j]
                else:
                    try:
                        first, last = height[j].split(",")
                    except ValueError:
                        if isInt(height[j]):
                            h = height[j]
                    else:
                        if isInt(first) and isInt(last):
                            h = height[j]
    if h != "":
        return h
    return "NA"


def get_width(data):
    entity_array = data["width"]
    for i in range(0, len(entity_array)):
        try:
            width = entity_array[i].split(" ")
        except ValueError:
            err = 0
        else:
            for j in range(0, len(width)):
                try:
                    first, last = width[j].split(",")
                except ValueError:
                    if isInt(width[j]):
                        return width[j]
                else:
                    if isInt(first) and isInt(last):
                        return width[j]
    return "NA"


def get_surface(data):
    entity_array = data["surface"]
    for i in range(0, len(entity_array)):
        try:
            surface = entity_array[i].split(" ")
        except ValueError:
            err = 0
        else:
            for j in range(0, len(surface)):
                if surface[j].strip() == "m\u00b2":
                    if isInt(surface[j - 1]):
                        return surface[j - 1]
    return "NA"


def get_date(data):
    entity_array = data["date"]
    for i in range(0, len(entity_array)):
        try:
            day, month, year = entity_array[i].split("/")
        except ValueError:
            err = 0
        else:
            if isInt(day) and isInt(month) and isInt(year):
                date = day + "/" + month + "/" + year
                return date
    return "NA"


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


"""
print(
    similar(
        "1 RUE COLBERT 13001 MARSEILLE ",
        "1 rue de la Joliette 13001 Marseille".upper(),
    )
)
"""
