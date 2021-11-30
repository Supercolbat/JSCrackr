import sys
import re

pattern = re.compile(r"\b0x[\dABCDEF]+", re.IGNORECASE)

file = sys.argv[-1]
with open(file) as f:
    source = f.read()

while True:
    match = pattern.search(source)
    if not match: break

    low, high = match.span()
    hex_string = source[low:high]
    source = re.sub(rf"\b{hex_string}\b", str(int(hex_string, 16)), source)

with open("output_"+file, "w+") as f:
    f.write(source)
