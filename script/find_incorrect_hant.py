#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json

import zhconv

data = {}

with open("../doc/hans_to_hant.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

incorrect_list = []
hant_list = []
character_to_line = {}

with open("../han_list.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line != "":
            character, explanations = line.split(" ", 1)
            character_to_line[character] = line
            hans = zhconv.convert(character, 'zh-hans')
            if hans in data:
                hant_list.extend(data[hans])

for hant in hant_list:
    if hant in character_to_line:
        incorrect_list.append(character_to_line[hant])
    else:
        incorrect_list.append(hant)

with open("../doc/incorrect_list.txt", 'w', encoding='utf-8') as f:
    f.writelines('\n'.join(incorrect_list))
