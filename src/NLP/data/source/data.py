import random
import string
import csv

type_rue = [
    "RUE",
    "PCE",
    "BOULEVARD",
    "SQUARE",
    "AVENENUE",
    "CENTRE",
    "CORNICHE",
    "COURS",
    "HYPODROME",
]
societes = [
    "LEROYMERLIN",
    "AUCHAN",
    "SUPERU",
    "SOFTAKA",
    "TRAITEUR",
    "INTERFLORA",
    "ROBERT",
    "BOUCHERIE",
    "LAVERIE",
    "BLANCHISSERIE",
    "HOTEL",
    "PIZZERIA",
    "INDEE",
    "CONCEPTION",
    "CHARCUTERIE",
    "DIDIER",
    "OLLYHOCK",
    "PATACREP",
    "NEXUS",
    "SHAMROCK",
]

"""
 "LE I-ORG\nLAURACEE",
    "RESTAURANT I-ORG\nLE I-ORG\n24",
    "LE I-ORG\nMELO",
    "BISTROT I-ORG\nO' I-ORG\nPRADO",
    "L' I-ORG\nEPUISETTE",
    "CHEZ I-ORG\nJEANOT",
    "AUX I-ORG\nANTIPODES",
    "BISTROT I-ORG\n13",
    "MADAME I-ORG\nJEANNE",
"""

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
arrondissements = [
    "13001",
    "13002",
    "13003",
    "13004",
    "13005",
    "13006",
    "13007",
    "13007",
    "13008",
    "13009",
    "13010",
    "13011",
    "13013",
    "13014",
    "13015",
]
debut_rue = [
    "ALBERT",
    "BENOIT",
    "ROGER",
    "MARQUIS",
    "ORIANT",
    "JOSEPH",
    "CAMILLE",
    "FRANCOIS",
    "ROBERT",
    "VICTOR",
    "ALAIN",
    "FABIEN",
    "PRADO",
    "PARADIS",
    "BOURSE",
    "BERTON",
    "BRAVET" "MICHEL",
    "PASCAL",
    "VIRGILE",
    "FERRARI" "NAU",
    "EMERY",
    "JEAN",
    "EDOUARD",
    "GILLES",
    "HELENE",
    "SAINT",
    "SEBASTIEN",
    "FELIX",
    "ANTOINE",
    "SAINTE",
    "MARGERITE",
    "RAYMOND",
    "JULES",
    "MARC",
    "AUDRIC",
    "RAPHAEL",
    "ROUSSEL",
]
fin_rue = [
    "",
    "",
    "",
    "DUPUIS",
    "HUGO",
    "GALLAN",
    "PAURIOL",
    "BAILLE",
    "GAULLE",
    "SAID",
    "KENEDY",
    "HOLLANDE",
    "MACON",
    "DESERT",
    "FRANGIN",
    "CHAVE",
    "MANIERE",
    "LACEPEDE",
    "TEISSERE",
    "HAGUEUNAU",
    "AMIS",
    "HEGER",
    "TIMONE",
    "LONGCHAMP",
    "PRADO",
    "LODI",
    "ASTRUC",
    "LOUBIERE",
    "FONTANGE",
    "CANEBIERE",
    "FIOCCA",
    "REPUBLIQUE",
    "CAISSERIE",
    "PASTEUR",
    "PHARO",
    "RIGAUD",
    "ROCHES",
]

surname = [
    "ROY",
    "MERCIER",
    "DUMAS",
    "MARTIN",
    "BRAHMI",
    "KADRI",
    "SEMERDJIAN",
    "BRUNET",
    "TURLEY",
    "BRETON",
    "MAYANT",
    "CURIE",
    "ROBERT",
    "FABRE",
    "COLOMB",
    "DJABARI",
    "FERDINAND",
    "COMBES",
    "COULOMB",
    "GASQUET",
    "GALSY",
    "LECLERC",
    "HOLLANDE",
    "GROSJEAN",
    "DELAUNE",
    "ROSE",
    "DUPUIS",
    "MAZZERANT",
    "GALLO",
    "GAILLARD",
    "NEMER",
    "BONNET",
    "CHAMPY",
    "LETREN",
]

first_name = [
    "Martin",
    "Julie",
    "Camille",
    "Julien",
    "Joseph",
    "Piere",
    "François",
    "Mohammed",
    "Kader",
    "Marie",
    "Jules",
    "Florian",
    "Eddy",
    "Anthony",
    "Fabien",
    "Mathieu",
    "Sébastien",
    "Alice",
    "Jean",
    "Joris",
    "Nicolas",
    "Yoan",
    "Kevin",
    "Albert",
    "Jacques",
    "Gilles",
    "Antoine",
    "Thierry",
    "Carlos",
    "Sylvain",
    "Karim",
    "Guillaume",
    "Boudjema",
    "Marine",
    "Chloe",
    "Ines",
    "Myriam",
    "Julia",
]


def numero_rue():
    return random.randint(1, 101)


def random_arrete():
    arr = random.randint(10, 500)
    if arr > 99:
        arrete = "%d_00%d" % (random.randint(2008, 2021), arr)
        return arrete
    else:
        arrete = "%d_000%d" % (random.randint(2008, 2021), arr)
        return arrete


def nom_famille():
    nom = random.choice(surname)
    return nom


def prenom():
    prenom = random.choice(first_name)
    return prenom


def random_year():
    j = random.randint(1, 31)
    m = random.randint(1, 12)
    a = random.randint(2009, 2020)
    jour = "%d" % j
    mois = "%d" % m
    annee = "%d" % a
    if j < 10:
        jour = "0%d" % j
    if m < 10:
        mois = "0%d" % m
    date = jour + "/" + mois + "/" + annee
    return date


def random_address(lower=True):
    epsilon = random.randint(1, 100)
    address = ""
    if epsilon > 30:
        address = "%d I-LOC\n" % numero_rue()
        address = address + random.choice(type_rue).lower() + " I-LOC\n"
        address = address + random.choice(debut_rue).lower() + " I-LOC\n"
        fin = random.choice(fin_rue).lower()
        if fin != "":
            fin = fin + " I-LOC\n"
        address = address + fin
        address = address + random.choice(arrondissements) + " I-LOC\n"
    else:
        with open(
            "loc_and_org.csv",
            "r",
        ) as file:
            reader = csv.reader(file)
            chosen_row = random.choice(list(reader))
            ad = chosen_row[5].split(" ")
            for x in ad:
                address = address + x + " I-LOC\n"
            address = address + random.choice(arrondissements) + " I-LOC\n"
    if lower:
        return address
    else:
        return address.upper()


def random_organisation(lower=True):
    epsilon = random.randint(1, 100)
    organisation = ""
    if epsilon > 30:
        organisation = random.choice(societes).lower() + " I-ORG\n"
        organisation = organisation + random.choice(type_societe).lower() + " I-ORG\n"
    else:
        with open(
            "loc_and_org.csv",
            "r",
        ) as file:
            reader = csv.reader(file)
            chosen_row = random.choice(list(reader))
            ad = chosen_row[4].split(" ")
            for x in ad:
                organisation = organisation + x + " I-ORG\n"
            organisation = organisation + random.choice(type_societe) + " I-ORG\n"
    if lower:
        return organisation
    else:
        return organisation.upper()


def random_dim():
    intOrNot = random.randint(0, 1)
    if intOrNot == 1:
        dim = "%d" % random.randint(1, 10)
    else:
        dim = "%d,%d0" % (random.randint(0, 10), random.randint(1, 9))
    return dim


def random_surface():
    dim = "%d" % random.randint(10, 80)
    return dim


def get_random_word():
    epsilon = random.randint(5, 10)
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(epsilon))
    return result_str
