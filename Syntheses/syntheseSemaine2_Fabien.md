I : Résumé sur mon utilisation de PD3F
II : Guide d'installation de PD3F 
III : Utilisation de l'API de PD3F
IV : Résultats

--------------------------------------------------------

I : Résumé

j'ai uniquement travaillé sur pd3f, en particulier avec l'API
l'API permet d'utiliser pd3f de la même façon que l'interface graphique mais cependant elle permet aussi un traitement automatisé du text généré, nous premettant ainsi de modifier l'output. Avec la version graphique il faut attendre que le texte soit généré et puis après on peut commencer à le traiter. Ici on peut intégrer l'API dans notre gestion de l'extraction pour éviter un trop grand nombres de manipulations.

--------------------------------------------------------

II: Guide d'installation de PD3F (MACOSX)

Cmd : git clone https://github.com/pd3f/pd3f
Installer docker https://hub.docker.com/editions/community/docker-ce-desktop-mac/ 
Cmd : brew install docker-compose
Cmd : cd pd3f 
Cmd : docker-compose up (Attendre la fin des téléchargements qui se lancent) *

Une fois que tout est indiqué dans la console comme téléchargé :
Ouvrir docker, normalement pd3f tourne en arrière plan
> ouvrir l'interface web
> Aller à http://localhost:1616/

* Optionnel : 
utiliser docker-compose up --scale worker=5
pour utiliser plus de workers

--------------------------------------------------------

III : Utilisation de l'API de PD3F 

voir test.py 

listes des paramètres :

lang: options de langues (options: 'de', 'en', 'es', 'fr')
fast: exécution plus rapide, on ne sait pas exactement lequel  (default: False)
tables: option pour récupérer les tableaux  (default: False)
experimental: option pour extraire le texte de façon expérimentales (footnotes to endnotes, depuplicate page header / footer) (default: False) /!\ pas utilisé
check_ocr: Option pour vérifier que les pages du pdf sont bien OCR (default: True, cannot be modified in GUI)

OCR = Reconnaissance Optique des Carractères

--------------------------------------------------------

IV - 2ème semaine / travail à venir

Temps de l'extraction de PDF :
--------------------------------------------------------
1er essai 
Lang: fr
Fast: False
tables: False
experimental: False
check_ocr: true
worker=5
nombre de page=250
TEMPS = 7m36s

--------------------------------------------------------

2ème essai
Lang: fr
Fast: False
tables: False
experimental: False
check_ocr: true
worker=1
nombre de page=250
TEMPS = 6m28s

--------------------------------------------------------

3ème essai
Lang: fr
Fast: False
tables: False
experimental: False
check_ocr: true
worker=3
nombre de page=250
TEMPS = 6m48s

--------------------------------------------------------


A venir : 

- Faire des tests sur les paramètres unique à PD3F (une sorte de grid search)
- essayer d'étendre ces recherches des meilleurs paramètres à parsr et pdfminer
