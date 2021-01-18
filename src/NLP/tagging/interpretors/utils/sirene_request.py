import os
import json
import requests  # faire un ' pip install requests '


headers = {
    "Accept": "application/json",
    "Authorization": "Bearer 9f26beba-289d-3fe6-a386-e1d9972eef0d",
}

"""
    purpose : get info to cross search adresses, names and such
    input : http request
    output : different info 
"""


def sirene_request(name):
    url = (
        "https://api.insee.fr/entreprises/sirene/V3/siren?q=periode(denominationUniteLegale%3A%22"
        + name
        + "%22)"
    )
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return "ErrRequest"


def get_siren_number(response):
    if response == "ErrRequest":
        return "NA"
    else:
        data = json.loads(response)
        return data["unitesLegales"][0]["siren"]


def get_creation_date(response):
    if response == "ErrRequest":
        return "NA"
    else:
        data = json.loads(response)
        return data["unitesLegales"][0]["dateCreationUniteLegale"]
