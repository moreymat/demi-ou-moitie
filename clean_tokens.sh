#bin/bash/!

for file in data/tokens/*; do
    [ -e "$file" ] || continue
    name=${file##*/}
    mv data/tokens/"$name" data/tokens/"${name:3}";
done
