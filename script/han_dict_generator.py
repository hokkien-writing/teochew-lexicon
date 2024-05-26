#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
from character.helpers import today
from character.core import Puj


def generate_han_dict(puj_list_file, han_dict_file):
    puj_map = {}
    with open(puj_list_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line != "":
                simple_puj, explanations = line.split(" ", 1)
                puj = Puj(simple_puj, explanations)
                puj_map[simple_puj] = puj

    with open(han_dict_file, 'w') as file:
        file.writelines(f'''# Rime dictionary
# encoding: utf-8
#
# Teochew Han 潮州話漢字
# 維護於 https://github.com/hokkien-writing/teochew-character/teochew.han.dict.yaml
#
---
name:	teochew.han
version:	"{today()}"
sort:	by_weight
use_preset_vocabulary:	true
import_tables:
  - teochew.puj
...
''')
        for simple_puj in puj_map:
            puj = puj_map[simple_puj]
            for han in puj.explanations:
                line = f"{han}\t{puj.keyboard()}\t100\n"
                file.write(line)


if __name__ == "__main__":
    generate_han_dict("../puj_list.txt",
                      "../teochew.han.dict.yaml")
    pass
