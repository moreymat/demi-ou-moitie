#!/bin/bash
scriptdir=`dirname "$BASH_SOURCE"`

rm data/tokens/*
rm data/out/*
#python3 -m venv venv
#source venv/bin/activate

echo "Extracting and segmenting pdf"
python3 src/extract_pdfplumber.py
python3 src/fuse_jsons.py
echo "extraction done\n"

python3 src/getTerrassesPizzas.py
python3 src/prepare_token.py
bash clean_tokens.sh
if [[ -d src/NLP/data/toPredict ]]
then
    rm src/NLP/data/toPredict/*.txt
else
    mkdir src/NLP/data/toPredict
fi
cp data/tokens/* src/NLP/data/toPredict/
cd src/NLP/
bash run.sh -f ../../data/tokens/ -t no -p yes
cd ../../
python3 src/add_geoloc.py
python3 src/toMap.py
