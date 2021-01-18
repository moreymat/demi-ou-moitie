##Première semaine :

Travail sur l'extracteur pd3f :
1. Commande à faire pour avoir travailler sur l'interface de pd3f
  - installer docker-compose : `sudo install docker-compose`
  - clonage du git : `git clone https://github.com/pd3f/pd3f`
  - ouvrir docker
  - dans le dossier pd3f faire `docker-compose up`
  - enfin aller sur la page : `http://localhost:1616/`

2. Résultat
  - Test de pd3f sur le fichier pdf de 152 pages avec les options : "fast mode" et "extract table"
  - résultats assez satisfaisants, pas de "trucs bizarres" apparents
  
  Travail sur parsr pour comparer les résultats avec Florian : extraction beaucoup trop longue, j'ai laissé parsr de cote pour me focus sur pd3f 

##Deuxieme semaine :

Travail sur l'extracteur pd3f :
1. Prise en main des différentes options pour évaluer les résultats de pd3f

2. Résultat
  - Test de pd3f sur le fichier pdf de 152 pages en enlevant l'option "fast mode"
  - résultats assez satisfaisants, pas trop de différences avec l'option "fast mode"
  
Travail commun avec les autres membres : appliquer pd3f sur la page 12 du pdf pour évaluer le visuel des différents extracteurs 
    
