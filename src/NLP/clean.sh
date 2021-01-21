#!/bin/bash
#Fabien GAILLARD

for file in data/toPredict/* ; do
    [ -e "$file" ] || continue
    grep . "$file" > temp
    cat temp > "$file"
done
