export OUTPUT_FILE="$1"

allennlp predict \
  --output-file $OUTPUT_FILE \
  --include-package tagging \
  --predictor enp_fr_predictor \
  --use-dataset-reader \
  --silent \
  /tmp/tagging/lstm/ \
  data/toPredict/"$2"
