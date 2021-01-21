import json
from allennlp.data.instance import Instance
from overrides import overrides
import ast
import itertools
import codecs


def string_escape(s, encoding="utf8"):
    return s.encode("utf8").decode(
        "unicode-escape"
    )


f = open("temp.txt", "w", encoding="latin-1")
with open("ajoutNER.txt", "r") as input_file:
    for lines in input_file:
        f.write(string_escape(lines))
f.close()

g = open("finalNERaddon.txt", "w")
with codecs.open("temp.txt", encoding="latin-1") as f:
    for line in f:
        g.write(line)
