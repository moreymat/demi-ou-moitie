#!/bin/bash
scriptdir=`dirname "$BASH_SOURCE"`

if [[ -d src/NLP/data/toPredict ]]
then
    rm src/NLP/data/toPredict/*.txt
else
    mkdir src/NLP/data/toPredict
fi
mkdir src/NLP/data/temp_for_extraction
unzip src/NLP/data/toPredict.zip -d src/NLP/data/temp_for_extraction/
cp src/NLP/data/temp_for_extraction/toPredict/*.txt src/NLP/data/toPredict/
rm -rf src/NLP/data/temp_for_extraction

cd src/NLP/
bash run.sh -f data/toPredict/ -t no -p yes
cd ../../
python3 src/add_geoloc.py
python3 src/toMap.py
