# Grandes lignes du projet

## Source

https://www.marseille.fr/mairie/conseil-municipal/recueil-des-actes-administratifs

## Étapes

1. Conversion du PDF en texte
    * entrée : PDF (voir `data/raw`)
    * format de sortie : texte brut, html, JSON (ex: https://github.com/axa-group/Parsr/blob/master/docs/json-output.md) ?
    * préparer des échantillons de sortie attendue pour réaliser des tests de qualité
    * définir des métriques et mettre en place une procédure de tests de qualité
    * tester et évaluer différents outils :
        * [pdfminer.six](https://github.com/pdfminer/pdfminer.six)
        * [Parsr](https://github.com/axa-group/Parsr)
        * [pd3f](https://github.com/pd3f/pd3f)
        * [pdfplumber](https://github.com/jsvine/pdfplumber)
    * difficultés : gestion de la mise en page (layout), nettoyage du document (enlever les en-têtes et pieds de page, reconstituer les mots en enlevant les césures...)
2. Segmentation du texte en arrêtés
    * définir les entrées / sorties sur des extraits des PDF exemples
    * évaluer la qualité de la segmentation
3. Classification des arrêtés
    * par délégation et/ou direction (pb: stabilité dans le temps ?)
    * par catégories : terrasse, pizza (dans un 1er temps)
    * heuristique? non-supervisée (clustering) ? supervisée? (scikit-learn)
4. Extraction des données des arrêtés
    * objectif : quel format et quel schéma pour la publication ?
    * exemples des jeux de donneés publiés à [Paris](https://www.data.gouv.fr/fr/datasets/etalages-et-terrasses/) et [Toulouse](https://data.toulouse-metropole.fr/explore/dataset/terrasses-autorisees-ville-de-toulouse/information/)
    * détection d'entités nommées : raison sociale du bénéficiaire, nature du commerce, adresse et dimensions de l'emplacement, type d'objet autorisé, dates etc,
        * spaCy ou textaCy ?
    * caractéristiques des emplacements
5. Enrichissement des données des arrêtés
    * Géolocalisation
        * [adresse.data.gouv.fr](https://adresse.data.gouv.fr/)
        * points d'intérêt OpenStreetMap
    * Liage des entités bénéficiaires avec la base SIRENE
6. Visualisation des données des arrêtés
    * afficher les données sur une carte interactive avec [folium](https://python-visualization.github.io/folium/), qui ressemble un peu à la [carte des terrasses de la ville de Paris](http://capgeo.sig.paris.fr/Apps/EtalagesTerrasses/)