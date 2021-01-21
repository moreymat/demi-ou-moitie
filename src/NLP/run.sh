#!/bin/bash
#Fabien GAILLARD
scriptdir=`dirname "$BASH_SOURCE"`
while getopts ":f:t:p:" opt; do
  case $opt in
    f) arg1="$OPTARG"  #CHEMIN VERS DOSSIER SOURCE CONTENANT LES ARRETES
    ;;
    t) arg2="$OPTARG"  #OPTION DE TRAIN (yes/no)
    ;;
    p) arg3="$OPTARG"  #OPTION DE PREDICTION (yes/no)
    ;;
    \?) echo "Invalid option -$OPTARG" >&3
    ;;
  esac
done

############################################################################

#TRAINING ET PREDICTION (si -p yes)


if [ "$arg2" == "yes" ]; then
    # ensure empty folder addons_train
    if [[ -d "$scriptdir"/data/source/addons_train ]]
    then
        rm "$scriptdir"/data/source/addons_train/*.txt
    else
        mkdir "$scriptdir"/data/source/addons_train
    fi
    # ensure empty folder addons_validation
    if [[ -d "$scriptdir"/data/source/addons_validation ]]
    then
        rm "$scriptdir"/data/source/addons_validation/*.txt
    else
        mkdir "$scriptdir"/data/source/addons_validation
    fi
    echo "Training & Predicting"
    echo 'Creating dataset ...'
    cd "$scriptdir"/data/source/
    python3 more_exs.py
    cd ../..
    echo '... Dataset successfully created'
    cat "$scriptdir"/data/source/addons_train/*.txt data/source/source_train.txt > data/train.txt
    echo 'Train set built'
    cat "$scriptdir"/data/source/addons_validation/*.txt data/source/source_validation.txt > data/validation.txt
    echo 'Validation set built'
    echo 'Training begins ...'
    allennlp train -f --include-package tagging -s "$scriptdir"//tmp/tagging/lstm "$scriptdir"/configs/train_lstm.jsonnet
    echo 'Training complete'
    if [ "$arg3" == "yes" ] ; then
        rm "$scriptdir"/data/predictions_raw/*.json
        rm "$scriptdir"/data/predictions/*.txt
        rm "$scriptdir"/terrasses.json #fichier contenant les instances de la carte
        echo '{"terrasses": []}' >> "$scriptdir"/terrasses.json
        echo 'Predicting ...'
        for file in data/toPredict/* ; do
            [ -e "$file" ] || continue
            name=${file##*/}
            base=${name%.txt}
            #script de prediction > fichiers JSON
            bash pred.sh "$scriptdir"/"data/predictions_raw/${base}.json" "${name}"
            #Convertisseur > fichiers txt au format [TOKEN LABEL]
            python3 "$scriptdir"/tagging/interpretors/utils/json2Txt.py "${base}.json"
            #Interpreteur > ajoute instances à terrasse.json
            python3 "$scriptdir"/tagging/interpretors/inter.py "${base}.txt"
        done
        echo 'Predictions located in data/predictions_raw and data/predictions'
    fi
    
############################################################################

#SEULEMENT PREDIRE

elif [ "$arg2" == "no" ] && [ "$arg3" == "yes" ]; then
    rm "$scriptdir"/data/predictions_raw/*.json
    rm "$scriptdir"/data/predictions/*.txt
    rm "$scriptdir"/terrasses.json #fichier contenant les instances de la carte
    echo '{"terrasses": []}' >> "$scriptdir"/terrasses.json
    echo "Just predicting ..."
    for file in data/toPredict/* ; do
        [ -e "$file" ] || continue
        name=${file##*/}
        base=${name%.txt}
        #script de prediction > fichiers JSON
        bash pred.sh "$scriptdir"/"data/predictions_raw/${base}.json" "${name}"
        #Convertisseur > fichiers txt au format [TOKEN LABEL]
        python3 "$scriptdir"/tagging/interpretors/utils/json2Txt.py "${base}.json"
        #Interpreteur > ajoute instances à terrasse.json
        python3 "$scriptdir"/tagging/interpretors/inter.py "${base}.txt"
    done
    echo 'Predictions located in data/predictions_raw and data/predictions'
    
############################################################################
    
else #USAGE
    echo -e '\nUsage error'
    echo -e '\nUSAGE : -f [path] -t [yes/no] -p [yes/no]\n'
    echo 'f : path to texts to predict'
    echo 't : training option'
    echo -e 'p : prediction option\n'
fi
