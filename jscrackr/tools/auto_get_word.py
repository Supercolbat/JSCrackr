import sys
import re

def log(message):
    if "-v" in sys.argv:
        print(message)

file = sys.argv[-1 - ("-v" in sys.argv)]
with open(file) as f:
    source = f.read()


ARG_AMOUNT = re.search(r"function _0x[\da-f]+\((.+?(?:, (.+?)))\) {", source).group(0).count(",") + 1
print("Amount of args:", ARG_AMOUNT)

returns_func_pattern = re.compile(r"function (_0x[\da-f]+)\(([^,]+)" + r", ([^,]+)"*(ARG_AMOUNT-1) + r"\) {\s+return (_0x[\da-f]+)\(([^,]+)" + r", ([^,]+)"*(ARG_AMOUNT-1) + r"\);\s*}\s*", re.IGNORECASE)
returns_get_pattern  = re.compile(r"function (_0x[\da-f]+)\(([^,]+)" + r", ([^,]+)"*(ARG_AMOUNT-1) + r"\) {\s+return get_word\(([^,]+?)(?:, .+?)?\);\s*}\s*", re.IGNORECASE)
args_pattern         =            r"(?<!function )%s\(([^),]+)" + r", ([^),]+)"*(ARG_AMOUNT-1) + r"\)"


# replace redirect functions
# function a(x, y, z) { b(y, x, z) }
# a(3, 2, 1)  ->  b(2, 3, 1)
log("== replacing redirects ==")
while True:
    match = returns_func_pattern.search(source)
    if not match: break

    groups = match.groups()

    p_name, *p_params = groups[:ARG_AMOUNT+1]
    c_name, *c_params = groups[ARG_AMOUNT+1:]

    # strip params
    p_params = [part.split()[0] for part in p_params]
    c_params = [part.split()[0] for part in c_params]

    log(f"Parent: {p_name} ({', '.join(p_params)})")
    log(f"Child : {c_name} ({', '.join(c_params)})")

    # get order
    # order = [4, ]
    # a, b, c, d, e
    # b, c, b, a, d
    order = []
    for param in p_params:
        positions = []
        while param in c_params:
            index = c_params.index(param)
            c_params[index] = None
            positions.append(index)
        order.append(positions)

    log(f"Order: {order}\n")

    # replace
    # [[3], [0, 2], [1], [4]]
    while True:
        match = re.search(args_pattern%p_name, source)
        if not match: break

        args = match.groups()
        new_args = [None] * ARG_AMOUNT

        for i, pos_list in enumerate(order):
            for pos in pos_list:
                new_args[pos] = args[i]

        source = re.sub(args_pattern%p_name, f"{c_name}({', '.join(new_args)})", source, 1)

    # remove
    source = returns_func_pattern.sub("", source, 1)

#with open("unfin_"+file, "w+") as f:
#    f.write(source)

# replace get_word functions
# function a(x, y, z) { get_word(y, z) }  ->  get_word(y)
log("\n== replacing get_word ==")
while True:
    # find function
    f_match = returns_get_pattern.search(source)
    if not f_match: break

    func_name, *params, replacer = f_match.groups()
    r_var, *replacer = replacer.split()  # b
    replacer = " ".join(replacer)        # - 644
    function = f_match.group()

    log({"func_name":func_name, "params":params, "r_var":r_var, "replacer":replacer})

    # find common arg
    for arg_index, common_arg in enumerate(params):
        # only get variable name  (_0xabc + 4, ...) -> _0xabc
        if common_arg.split()[0] == r_var:
            break

    # find all mentions of function
    while True:
        a_match = re.search(args_pattern%func_name, source)
        if not a_match: break

        lo, hi = a_match.span()
        args = a_match.groups()

        # replace
        source = source[:lo] + f"get_word({args[arg_index] + replacer})" + source[hi:]

    # remove from source
    source = returns_get_pattern.sub("", source, 1)

with open("output_"+file, "w+") as f:
    f.write(source)
