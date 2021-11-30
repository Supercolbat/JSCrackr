"""
    const _0x4abc23 = {
        'DNVwv': "KfWtw",
        'POPyR': "Qihna",
        'DbxcU': "(((.+)+)+)+$",
        'TCadY': function (_0x41c719) {
            return _0x41c719();
        },
        'NUPjD': function (_0x2a8e23, _0x292626) {
            return _0x2a8e23 - _0x292626;
        },
        'yyedh': function (_0x3e3a4a, _0x28bb4b) {
            return _0x3e3a4a >= _0x28bb4b;
        },
        'hJlWE': function (_0x255010, _0x2475ad) {
            return _0x255010 === _0x2475ad;
        },
        'HTZmo': "wlnTK"
    };
"""

import re
import sys

file = sys.argv[-1]
with open(file) as f:
    source = f.read()

str_pattern       = re.compile(r"\s*'(\w+)': ('.+?'),?")
func_pattern_op   = re.compile(r"\s*'(\w+)': function \((_0x[\da-f]+), _0x[\da-f]+\) {\s*return (_0x[\da-f]+) (.+?) _0x[\da-f]+;\s*},?")
func_pattern_call = re.compile(r"\s*'(\w+)': function \(_0x[\da-f]+\) {\s*return _0x[\da-f]+\(\);\s*},?")

matches = re.finditer(r"\s*const (_0x[\da-f]+) = {(.+?)};", source, re.DOTALL)
for match in matches:
    name, all_pairs = match.groups()
    low, high = match.span()

    # replace strings
    pairs = str_pattern.finditer(all_pairs)

    for pair in pairs:
        key, value = pair.groups()
        source = re.sub(rf"\b{name}\['{key}'\]", value, source)
        source = source.replace(pair.group(), "")

    # replace functions (operators)
    pairs = func_pattern_op.finditer(all_pairs)

    for pair in pairs:
        key, a, b, op = pair.groups()
        source = re.sub(
            rf"\b{name}\['{key}'\]\((.+?), (.+?)\)",
            " ".join([r"\1", op, r"\2"][::~-(a == b) * 2 + 1]), # rf"\1 {op} \2" if true
            source                                              # rf"\2 {op} \1" if false
        )
        source = source.replace(pair.group(), "")

    # replace functions (call)
    pairs = func_pattern_op.finditer(all_pairs)

    for pair in pairs:
        key = pair.groups(0)
        source = re.sub(rf"\b{name}\['{key}'\]\((.+?)\)", r"\1()", source)
        source = source.replace(pair.group(), "")

with open("output_"+file, "w+") as f:
    f.write(source)
