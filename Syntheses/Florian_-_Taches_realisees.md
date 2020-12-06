#Florian tâches réalisées

##Première semaine :

Travail sur l'extracteur pdf parsr :
1. Commande à faire pour avoir travailler sur l'interface de parsr
  - installer docker-compose : `sudo install docker-compose`
  - clonage du git : `git clone https://github.com/axa-group/Parsr`
  - aller à la racine de parsr et faire `sudo docker pull axarev/parsr-ui-localhost`
  - Une fois que tout est installé, faire `sudo docker run -t -p 8080:80 axarev/parsr-ui-localhost:latest`
  - Ensuite, il suffit d'ouvrir une page web et aller sur `http://localhost:8080`

2. Travail fait
  - J'ai lancé parsr sur un pdf de 60 pages avec full options, j'ai laissé tourner 24h et pas de résultat0

##Deuxième semaine :

Travail toujours sur l'extracteur parsr et l'extracteur pd3f.

- Commande pour utiliser l'interface de pd3f
  - clonage du git `git clone https://github.com/pd3f/pd3f`
  - aller à la racine de parsr et faire `sudo docker-compose up`
  - Ensuite, il suffit d'ouvrir une page web et aller sur `http://localhost:1616`
  
- Après j'ai réussi à trouver les options qu'utilise pd3f pour parsr.
  
- Liste des options : 
  - out-of-page-removal
  - whitespace-removal
  - redundancy-detection
  - header-footer-detection
  - world-to-line-new
  - reading-ordre-detection
  - lines-to-paragraph
  - page-number-detection
  - hierarchy-detection

- J'ai lancé parsr avec ces options sur un pdf de 152 pages et j'ai eu un résultat en un peu moins de 20 minutes.
