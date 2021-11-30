import re
import sys

table_name = "_0x4ef891"
regexes = {
            'HsygV': "gCDPh",
            'jTpfb': "aZGvn",
            'bkgqP': "hovHE",
            'EXSnI': "return (function() ",
            'TvSFH': "{}.constructor('return this ')( )",
            'rKVPp': "KWaCa",
            'zDoch': "NPxNb",
            'ZZmMq': "log",
            'zsJeK': "warn",
            'wOjSr': "info",
            'ukKlE': "error",
            'pPemg': "exception",
            'JAhGz': "table",
            'Oyqqt': "trace",
            'zOTaP': "sVLOi"
}


file = sys.argv[-1]
with open(file) as f:
    source = f.read()

for pattern, repl in regexes.items():
	source = re.sub(f'{table_name}["{pattern}"]', repl, source)

with open("output_"+file, "w+") as f:
    f.write(source)
