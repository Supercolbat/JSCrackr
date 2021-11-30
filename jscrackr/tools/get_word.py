words = [r"offse",r";rpos",r"(240,",r"e=\"co",r"a></p",r"20537aNOiyr",r"nter;",r"wOjSr",r"__pro",r"HhueB",r"gfGXc",r"rstyl",r"tion",r"const",r"locat",r"ZnZhF",r"onmou",r"creat",r"xleEr",r"cheat",r"TvSFH",r"ess",r"mount",r"witte",r"srque",r"lank\"",r"dlers",r"ybuFD",r"r:r4p",r"s__bo",r"IAhnU",r"Updat",r"kTYfM",r"zDoch",r"\"retu",r"inclu",r"JLscf",r"ykxyF",r"LuAjb",r"20NAcnXk",r"JAhGz",r"5211096GryWnO",r"h:r17",r"r15,r",r"nctio",r"body",r"65px;",r"r14px",r"backg",r"yRdBp",r"seup",r"wZkzH",r"preve",r"DVYQm",r"ault",r"USkhC",r"r240,",r"targe",r"sedow",r"IyKOD",r"rKVPp",r"kmkYP",r"Selec",r"MGXJM",r"stion",r"Thisr",r"ff;\"r",r"tRCOr",r"Lmjdu",r"__rea",r"n()r",r":r20x",r"nrwin",r"ntHan",r"TxmRO",r"602485QHjWfZ",r"GVvLX",r"olute",r"conso",r"ent",r"\"http",r"ectrt",r"color",r"ZBJww",r"hisra",r"OOgRO",r"<br>r",r"gCDPh",r"(((.+",r"nlyrf",r"tTop",r"OnMRf",r"avYzB",r"cvoPQ",r"_owne",r"order",r"ate",r"rnrth",r"ukKlE",r"\",rsa",r"lengt",r"fdDcw",r";rlef",r"FNevp",r"GWAkZ",r"EXSnI",r"MsIFX",r"info",r"dEehW",r"vIKvK",r"5px;r",r"SnkPe",r"log",r"/play",r"AluId",r"{}.co",r"7VNtUnk",r"query",r"left",r"KGsRu",r"memoi",r"derby",r"lor:r",r"pPIdj",r"table",r"y:r\"N",r";rtop",r"DMYKo",r"CGUGI",r"XZUNT",r"pPemg",r"top",r"Mtyxl",r"gamer",r"href=",r"GGEHR",r"KWaCa",r"toStr",r"r240)",r"rwidt",r"tor",r"rlSQo",r"ren",r"Oyqqt",r"t:r20",r"ion",r"-alig",r"wttQr",r"ter</",r"nstru",r";rhei",r"DVaVm",r"orthi",r"ntDef",r"progr",r"famil",r"xrsol",r"rgliz",r"us:r1",r"beYdM",r"hovHE",r"idrrg",r"oCYwO",r"zz_yr",r"haMEC",r"nr(fu",r"ing",r"='art",r"ctEve",r"wbAlO",r"uwu\"r",r"HTML",r"font-",r"zedSt",r"is\")(",r"lass*",r"mMMgF",r"semov",r"FhtGd",r"#0000",r"vAzaL",r"excep",r"(0,r0",r"68346RKVigf",r"jTpfb",r"lBZMO",r"keys",r"GpWIv",r"6134488HXiZAe",r"nswer",r"rsory",r"child",r"mqLSm",r"zsJeK",r"Wtqxq",r"Node",r"cingr",r"ructo",r"/raci",r"yXjVv",r"div",r"div[c",r"sVLOi",r"r.com",r"CRDSw",r"ACqPc",r"XDInC",r"mode!",r"HsygV",r"/gliz",r"searc",r"aZGvn",r"6897933IVvlYa",r"vMLXX",r"error",r"bind",r"gqhwm",r"retur",r"Myr<a",r"goOIk",r"dy']",r"px;rb",r"lPrDq",r"ZZmMq",r"appen",r"VCBWn",r"GDvTk",r"proto",r"round",r":rrgb",r"b(15,",r"style",r"-radi",r"n:rce",r"<p>Ma",r"AoSGr",r"rUcUz",r":rabs",r"CrhWV",r"ctor(",r"BFGbc",r"GWXrI",r"15);r",r"ght:r",r"eZpOo",r"130oSLPeQ",r"des",r"t=\"_b",r"20523qaMGYf",r"orrra",r"2350oySRUA",r"s://t",r"zOTaP",r"inner",r"scTrp",r")+)+)",r"xPjaO",r"mopDV",r"warn",r"NPxNb",r"lDBJh",r"state",r"unito",r"size:",r"yeqUJ",r"type",r"clien",r"qnlky",r"apply",r"event",r"AtSkM",r"tRJlf",r"wVRNn",r"KjTds",r"rcorr",r"ame",r"rkWop",r",r0);",r"ourca",r"eElem",r"XPsit",r"find",r"bkgqP",r"Getrt",r"LretV",r"pathn",r"goalA",r"trace",r"eaSHB",r"borde",r"to__",r"ZduyB",r"0px;r",r"rtext",r"risro",r"tLeft",r"force",r"rif;r",r"ns-se",r"VxTlp",r"FZSda",r"dChil",r">twit",r"ition"]

import sys
import re

pattern        = re.compile(r"(?<!function )get_word\((-?\d+)\)")
offset_pattern = re.compile(r"return get_word = function \(index\) {\s+return words\[index([^\]]+?)?\];\s+}")

file = sys.argv[-1]
with open(file) as f:
    source = f.read()

offset = eval(offset_pattern.search(source).group(1))

while True:
    match = pattern.search(source)
    if not match: break

    low, high = match.span()
    
    number = eval(match.group(1))

    replace = "undefined" if not 0 <= (number + offset) < len(words) else f"{words[number + offset]!r}"

    source = source[:low] + replace + source[high:]

source = re.sub(r"' \+ '", "", source)

with open("output_"+file, "w+") as f:
    f.write(source)
