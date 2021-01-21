# NER

## 1) Architecture du dossier

NER/
|- tagging/
  |- readers/
    |- __init__.py
    |- enp_fr_reader.py  -> Dataset Reader
  |- models/
    |- __init__.py
    |- lstm.py                 -> Model
  |- __init__.py
|- data/ ...
    |- train.txt
    |- validation.txt
    |- pred.txt                 -> fichier utilisé pour la prédiction dans pred.sh
    |- source/
        |- more_exs.py         -> A COMPLETER, crée plus d'exemples au format "TOKEN LABEL", les sauvegarde dans addons/
        |- pre_process.py     -> fonction à cause des problèmes d'encodage au niveau des fichiers json
        |- touslesarretes.json    -> pas encore présent mais ça sera le fichier source
        |- json2enp.py     -> A DEV, fonction permettant de transformer les arrêtés au format pour la predictions "TOKEN O"
        |- addons/ ...       -> contient toutes instances générées au format "TOKEN LABEL"
|- configs/
    |- train_lstm.jsonnet -> fichier contanant notamment les infos du path pour les fichiers train.txt et validation.txt
|- allennlp/ ...
|- predictions.json       -> prédictions d'un texte brutes
|- test.txt                     -> mêmes prédictions mais plus simples à lire
|- pred.sh                    -> script pour faire une prédiction

## 2) installations à faire

pip install allennlp
pip install allennlp-models
pip install -r dev-requirements.txt (dans allennlp/)

sinon voir :
<https://github.com/allenai/allennlp>

### Voir 5) pour tout lancer d'un coup

## 3) Générer les fichiers nécessaires

### Générer des fichiers supplémentaires pour train et validation

> python3  more_exs.py  
(depuis data/source/ pour éviter pb de chemin)

### Concatener tous les addons_trains.txt avec le fichier source_train.txt  (idem avec validation)

> cat data/source/addons_train/*.txt data/source/source_train.txt > data/train.txt
> cat data/source/addons_validation/*.txt data/source/source_validation.txt > data/validation.txt

## 4) comment train & prédire ?

1. Train le model  

   > allennlp train -f --include-package tagging -s /tmp/tagging/lstm configs/train_lstm.jsonnet

   * s'il y a une erreur, ça peut être du à un problème au niveau des chemins des datasets)
   * Lors de la première exécution, ça télécharge un fichier (Glove word embeddings 800Mo env)

2. Prédiction

   > bash pred.sh ou bash run.sh 1 (ne pas oublier l'argument, sinon ça train aussi)

   * Il faut avoir un input au format "TOKEN O"
   * chemin du fichier input à changer dans pred.sh
   * Ne pas avoir de Label différent de ceux de la liste

## 5) Génération, train et prédiction avec une seule commande

> bash run.sh > training + prediction
> bash run.sh 1 > prediction seulement

## 6)  Ce qui reste à faire

### a) more_exs.py

* faire en sorte d'enrichir  ' more_exs.py ' train sur plusieurs types d'arrêtés différents (relatifs aux terrasses & camions)

on retrouve les infos intéressantes dans :

['title']['text']   -> en gros ce qui se trouve juste en dessous de "admin1" et "admin2"
['intros'][0]['text'] & ['intros'][1]['text']   -> contient les arrêtés

['intros'][0]['text']  -> contient les infos sur le bénéficiaire (nom + nom société + adresse )

['articles'][0]['text']  -> contient des infos sur la terrasse

* plus, voir pour camions pizza

> en gros : s'inspirer de la fonction déjà faite pour générer des nouveaux arrêtés pour bien train

### b) fonction pour extraire et transformer les arrêtés au format "TOKEN LABEL"

LABEL = O dans ce cas là puisqu'il s'agit de la prédiction

faire en sorte de générer un fichier unique par terrasse ou camion

### c) fonction pour transformer l'output de la prédiction en fichiers json au format défini par Florian

## 7) Liste des Labels

I-LOC : Adresse

I-PER : Personne

I-ORG : Société

I-DAT : Date

I-ART : Article

I-CMP : n° compte

I-DMD : n° demande

----------------- Relatifs aux terrasses

I-SAI : Saillie

I-LRG : Largeur

I-SUP : Superficie
