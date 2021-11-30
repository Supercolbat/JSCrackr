#!/bin/bash
echo "Make sure you have updated the word list in tools/get_word.py"

python3 tools/setup.py $1

python3 tools/unhex.py output_$1
mv output_output_$1 output_$1

python3 tools/auto_get_word.py output_$1
mv output_output_$1 output_$1

python3 tools/math.py output_$1
mv output_output_$1 output_$1

python3 tools/get_word.py output_$1
mv output_output_$1 output_$1

python3 tools/dict.py output_$1
mv output_output_$1 result_$1
rm output_$1