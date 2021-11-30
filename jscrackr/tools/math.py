import sys
import re

pattern = re.compile(r"(?:\b|-)((?:-?\d+ ?[-+*] ?)+-?\d+)\b")

file = sys.argv[-1]
with open(file) as f:
    source = f.read()

while True:
    match = pattern.search(source)
    if not match: break

    low, high = match.span()
    expression = source[low:high]
    source = source[:low] + str(eval(expression)) + source[high:]

with open("output_"+file, "w+") as f:
    f.write(source)
