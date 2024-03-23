#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
from script.common import to_keyboard_puj, today


def generate_han_dict(from_path, to_path):
    puj_to_characters = {}
    with open(from_path, 'r') as file:
        for line in file:
            line = line.strip().lower()
            if line:
                puj, *characters = line.split()
                puj_to_characters[to_keyboard_puj(puj)] = characters

    with open(to_path, 'w') as file:
        file.writelines(f'''# Rime dictionary
# encoding:	utf-8
#
# Teochew Han 潮州話漢字
# 維護於 https://github.com/tsunhua/teochew-character/teochew.han.dict.yaml
#
---
name:	teochew.han
version:	"{today()}"
sort:	by_weight
use_preset_vocabulary:	false
...
''')
        for puj in puj_to_characters:
            for ch in puj_to_characters[puj]:
                line = f"{ch}\t{puj}\n"
                file.write(line)


if __name__ == "__main__":
    generate_han_dict("../同音字表-按羅馬字分組.txt",
                      "../teochew.han.dict.yaml")
    pass
