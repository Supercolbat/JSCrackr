"""
TODO: Automatically remove defending mechanism


        _0x5b7fb5 = _0x324bbd(this, function () {
            function _0x43255f(_0x1e8d35, _0xce5ffd, _0x4edbbb, _0x8fee4c) {
                return _0x26584d(_0x1e8d35, _0xce5ffd - 418, _0x4edbbb - 457, _0x8fee4c - -882);
            }

            function _0x22a533(_0x43e239, _0x317fee, _0x4f6a5d, _0x207ba4) {
                return _0x26584d(_0x207ba4, _0x317fee - 20, _0x4f6a5d - 268, _0x317fee - -1012);
            }
            if ('Qihna' === _0x4abc23['POPyR']) return _0x5b7fb5[_0x22a533(-374, -358, -358, -349)]()[_0x22a533(-370, -354, -362, -366)](_0x4abc23[_0x22a533(-350, -351, -352, -351)])['toString']()[_0x22a533(-347, -347, -341, -356) + 'r'](_0x5b7fb5)[_0x22a533(-348, -354, -361, -362)](_0x4abc23[_0x22a533(-358, -351, -341, -356)]);
            else _0x3150d4 += _0x16d9e6[_0x15009];
        });
    _0x4abc23[_0x26584d(667, 661, 662, 667)](_0x5b7fb5);

"""

import re
import sys

word_list_pattern = re.compile(r"function (_0x[\da-f]+)\(\).+?= (\[(?:['\"][^\n]+['\"](?:, ['\"][^\n]+?(?<!\\)['\"])*)\]).+?}.+?}", re.DOTALL)
get_word_pattern  = re.compile(r"function (_0x[\da-f]+)\(_0x[\da-f]+, _0x[\da-f]+\) {\s+const _0x[\da-f]+.+?_0x[\da-f]+ (- [^;]+);.+?}.+?}", re.DOTALL)

word_list_replacer = """\
function word_list() {{
    const words = {};
    word_list = function () {{
        return words;
    }};
    return word_list();
}}
"""

get_word_replacer = """\
function get_word(index, command) {{
    const words = word_list();
    return get_word = function (index) {{
        return words[index {}];
    }}, get_word(index);
}}
"""

file = sys.argv[-1]
with open(file) as f:
    source = f.read()

# replace word_list
match = word_list_pattern.search(source)
name, words = match.groups()
source = word_list_pattern.sub(word_list_replacer.format(words), source)
source = re.sub(rf"\b{name}\b", "word_list", source)

# replace get_word
match = get_word_pattern.search(source)
name, math = match.groups()
source = get_word_pattern.sub(get_word_replacer.format(math), source)
source = re.sub(rf"\b{name}\b", "get_word", source)

# other regex
#source = re.sub(r"'(\d+)\w+'", r"'\1'", source)

# ![] !![]
r"""
matches = re.finditer(r"\s+let (_0x[\da-f]+) = (!!?\[\]);", source)
for match in matches:
    name, value = match.groups()
    source = re.sub(rf"(?<!let )\b{name}\b", value, source)
    source = source.replace(match.group(), "")
"""

source = source.replace("!![]", "true")
source = source.replace("![]", "false")

with open("output_"+file, "w+") as f:
    f.write(source)
