import folium
import json
import math


# Vérifie que les coordonnées sont bien dans marseille
def store_in_marseille(x, y):

    cx = 43.2961743
    cy = 5.3699525


    if math.sqrt((x - cx) ** 2 + (y - cy) ** 2) < 0.15:
        return True
    else:
        return False


# Input: json file
# Output: Interactive map as HTML
def get_interactive_map(json_path):
    with open(json_path) as json_file:
        data = json.load(json_file)

    m = folium.Map(
        location=[43.2961743, 5.3699525], tiles="Stamen Terrain", zoom_start=13
    )

    if "terrasses" in data.keys():
        for store in data["terrasses"]:

            if store_in_marseille(store["locs"][0], store["locs"][1]):

                marker_html = "<b>"

                if store["societe"] != "NA":
                    marker_html += store["societe"] + "</b><b>   |   TERRASSE</b><br>"

                if store["adresses"] != "NA":
                    marker_html += "<b>Adresse:</b> " + store["adresses"]

                if store["facade"] != "NA":
                    marker_html += (
                        "<br><b>Taille de façade:</b> " + str(store["facade"]) + " m"
                    )

                if store["largeur"] != "NA":
                    marker_html += "<br><b>Largeur:</b> " + str(store["largeur"]) + " m"

                if store["superficie"] != "NA":
                    marker_html += (
                        "<br><b>Superficie:</b> " + str(store["superficie"]) + " m²"
                    )

                if store["date"] != "NA":
                    marker_html += "<br><b>Date de l'arrété:</b> " + store["date"]

                folium.Marker(
                    store["locs"],
                    popup=folium.Popup(
                        marker_html,
                        max_width=1000,
                    ),
                    tooltip="<b>" + store["societe"] + "</b>",
                    icon=folium.Icon(color="blue", icon="university", prefix="fa"),
                ).add_to(m)

    if "pizza" in data.keys():
        for store in data["pizza"]:
            for i, loc in enumerate(store["locs"]):

                marker_html = "<b>"

                if store["societe"] != "NA":
                    marker_html += (
                        store["societe"] + "</b><b>   |   Camion Pizza</b><br>"
                    )

                if store["adresses"] != "NA":
                    marker_html += "<b>Adresse:</b> " + store["adresses"][i]

                if store["date"] != "":
                    marker_html += "<br><b>Date de l'arrété:</b> " + store["date"]

                folium.Marker(
                    loc,
                    popup=folium.Popup(
                        marker_html,
                        max_width=300,
                    ),
                    tooltip="<b>" + store["societe"] + "</b>",
                    icon=folium.Icon(color="red", icon="truck", prefix="fa"),
                ).add_to(m)
    return m


if __name__ == "__main__":
    map = get_interactive_map(
        r"data/out/geoloc.json"
    )
    map.save("index.html")
