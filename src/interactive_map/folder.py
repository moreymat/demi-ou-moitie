import folium
import json

with open(
    r"C:\Users\Anthony\Downloads\demi-ou-moitie-main\src\interactivemap\json_test.json"
) as json_file:
    data = json.load(json_file)

m = folium.Map(location=[43.2961743, 5.3699525], tiles="Stamen Terrain", zoom_start=13)

m.add_child(folium.LatLngPopup())

for store in data:

    if store["type"] == "terrasse":

        marker_html = (
            "<b>"
            + store["societe"]
            + "</b><b>   |   TERRASSE</b><br><b>Adresse:</b> "
            + store["adresses"][0]
        )

        if store["adresses"][1] != "":
            marker_html += "<br><b>Adresse 2:</b> " + str(store["adresses"][1])

        if store["facade"] != 0:
            marker_html += "<br><b>Taille de façade:</b> " + str(store["facade"]) + " m"

        if store["largeur"] != 0:
            marker_html += "<br><b>Largeur:</b> " + str(store["largeur"]) + " m"

        if store["superficie"] != 0:
            marker_html += "<br><b>Superficie:</b> " + str(store["superficie"]) + " m"

        if store["date"] != "":
            marker_html += "<br><b>Date d'ouverture:</b> " + store["date"]

        folium.Marker(
            store["locs"],
            popup=folium.Popup(
                marker_html,
                max_width=1000,
            ),
            tooltip="<b>" + store["societe"] + "</b>",
            icon=folium.Icon(color="blue", icon="university", prefix="fa"),
        ).add_to(m)

    if store["type"] == "pizza":
        for i, loc in enumerate(store["locs"]):

            marker_html = (
                "<b>"
                + store["societe"]
                + "</b><b>   |   CAMION PIZZA</b><br><b>Adresse:</b> "
                + store["adresses"][i]
            )

            if store["date"] != "":
                marker_html += "<br><b>Date d'ouverture:</b> " + store["date"]

            folium.Marker(
                loc,
                popup=folium.Popup(
                    marker_html,
                    max_width=300,
                ),
                tooltip="<b>" + store["societe"] + "</b>",
                icon=folium.Icon(color="red", icon="truck", prefix="fa"),
            ).add_to(m)

m.save("index.html")
