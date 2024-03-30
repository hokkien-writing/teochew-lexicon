#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json

import zhconv

data = {}

with open("../doc/hans_to_hant.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

amend_list = []
delete_characters = []
all_lines = []

with open("../han_list.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line != "":
            all_lines.append(line)
            character, explanations = line.split(" ", 1)
            hans = zhconv.convert(character, 'zh-hans')
            if hans in data:
                delete_characters.extend(data[hans])

with open("../doc/correct_list.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line.startswith('//'):
            ch = line.lstrip('//').split(' ', 1)[0]
            delete_characters.append(ch)
        elif line != "":
            character, explanations = line.split(" ", 1)
            amend_list.append(line)

keep_lines = []

with open("../han_list.txt", 'w', encoding='utf-8') as f:
    for line in all_lines:
        line = line.strip()
        if line != "":
            character, explanations = line.split(" ", 1)
            if character not in delete_characters:
                keep_lines.append(line)
    for a in amend_list:
        keep_lines.append(a)

    f.writelines('\n'.join(keep_lines))