import json

"""
    purpose : evaluate results, it's very basic, the obvious limitations are that this can't tell whether any data is accurate, we're just checking if it exists"
    input : JSON file containing the data
    output : prints score of each entity and how many times it exists
"""


with open("terrasses.json") as f:
    data = json.load(f)
    nbt = len(data["terrasses"])
    ad = 0
    sc = 0
    dt = 0
    hg = 0
    wd = 0
    sf = 0
    sn = 0
    cr = 0
    for i in range(len(data["terrasses"])):
        # organisation
        if data["terrasses"][i]["societe"].strip() == "NA":
            sc = sc + 1
        score_sc = sc / len(data["terrasses"])
        # address
        if data["terrasses"][i]["adresses"].strip() == "NA":
            ad = ad + 1
        score_ad = ad / len(data["terrasses"])
        # date
        if data["terrasses"][i]["date"].strip() == "NA":
            dt = dt + 1
        score_dt = dt / len(data["terrasses"])
        # height
        if data["terrasses"][i]["facade"].strip() == "NA":
            hg = hg + 1
        score_hg = hg / len(data["terrasses"])
        # width
        if data["terrasses"][i]["largeur"].strip() == "NA":
            wd = wd + 1
        score_wd = wd / len(data["terrasses"])
        # surface
        if data["terrasses"][i]["superficie"].strip() == "NA":
            sf = sf + 1
        score_sf = sf / len(data["terrasses"])
        # Siren Number
        if data["terrasses"][i]["SIREN"].strip() == "NA":
            sn = sn + 1
        score_sn = sn / len(data["terrasses"])
        # Creation date
        if data["terrasses"][i]["date_creation"].strip() == "NA":
            cr = cr + 1
        score_cr = cr / len(data["terrasses"])

    score = nbt - sc
    print(
        f"\n nombre societes corrects: {score} sur {nbt},         err en  % : {score_sc} "
    )
    score = nbt - ad
    print(
        f"\n nombre adresses corrects: {score} sur {nbt},         err en  % : {score_ad}"
    )
    score = nbt - dt
    print(
        f"\n nombre dates correctes: {score} sur {nbt},           err en  % : {score_dt} "
    )
    score = nbt - hg
    print(
        f"\n nombre facade corrects: {score} sur {nbt},           err en  % : {score_hg} "
    )
    score = nbt - wd
    print(
        f"\n nombre largeur corrects: {score} sur {nbt},          err en  % : {score_wd} "
    )
    score = nbt - sf
    print(
        f"\n nombre superficie corrects: {score} sur {nbt},       err en  % : {score_sf}"
    )
    score = nbt - sn
    print(
        f"\n nombre numero siren corrects: {score} sur {nbt},     err en  % : {score_sn}"
    )
    score = nbt - cr
    print(
        f"\n nombre date de creation corrects: {score} sur {nbt}, err en  % : {score_cr}"
    )
