import json
import sys

input_path = "data/predictions_raw/" + sys.argv[1]
output_path = "data/predictions/" + sys.argv[1].split(".")[0] + ".txt"
with open(input_path) as f:
    data = json.load(f)


output = open(output_path, "w")

for i in range(len(data["tokens"])):
    output.write(data["tokens"][i] + " " + data["predicted"][i] + "\n")

output.close()
