#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
from character.helpers import today
from character.core import Puj


def generate_puj_dict(puj_list_file, puj_dict_file):
    with open(puj_dict_file, 'w') as file:
        file.writelines(f'''# Rime dictionary
# encoding: utf-8
#
# Teochew PUJ 潮州白話字
# 維護於 https://github.com/tsunhua/teochew-character/teochew.puj.dict.yaml
#
---
name:	teochew.puj
version:	"{today()}"
sort:	by_weight
use_preset_vocabulary:	false
...
''')
        with open(puj_list_file, 'r') as f:
            lines = f.readlines()
            puj_without_tone_list = []
            for line in lines:
                line = line.strip()
                if line != "":
                    simple_puj, explanations = line.split(" ", 1)
                    if simple_puj.strip() == '':
                        continue
                    puj_without_tone = simple_puj[:len(simple_puj) - 1]
                    puj_without_tone_list.append(puj_without_tone)
            puj_without_tone_list = sorted(set(puj_without_tone_list))
            for puj_without_tone in puj_without_tone_list:
                if puj_without_tone.endswith('h') \
                        or puj_without_tone.endswith('p') \
                        or puj_without_tone.endswith('t') \
                        or puj_without_tone.endswith('k'):
                    for tone in ['4', '8']:
                        write_dict_line(Puj(puj_without_tone + tone), file)
                else:
                    for tone in ['1', '2', '3', '5', '6', '7']:
                        write_dict_line(Puj(puj_without_tone + tone), file)


def write_dict_line(puj, file):
    line = f"{puj.handwriting()}\t{puj.keyboard()}\n"
    file.write(line)
    line = f"{puj.handwriting().capitalize()}\t{puj.keyboard().capitalize()}\n"
    file.write(line)


if __name__ == "__main__":
    generate_puj_dict("../puj_list.txt", "../teochew.puj.dict.yaml")
    pass
