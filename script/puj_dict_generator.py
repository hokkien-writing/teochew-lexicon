#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
from script.common import to_keyboard_vowel, simplify_tone, keyboard_to_handwriting_puj, today


def generate_puj_dict(from_path,to_path):
    with open(to_path, 'w') as file:
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
        with open(from_path, 'r') as f:
            lines = f.readlines()
            puj_without_tone_list = []
            for line in lines:
                puj = line.split()[0]
                puj = to_keyboard_vowel(puj)
                puj_without_tone = puj[:len(puj) - 1]
                puj_without_tone_list.append(puj_without_tone)
            puj_without_tone_list = sorted(set(puj_without_tone_list))
            for puj_without_tone in puj_without_tone_list:
                if puj_without_tone.endswith('h') \
                        or puj_without_tone.endswith('p') \
                        or puj_without_tone.endswith('t') \
                        or puj_without_tone.endswith('k'):
                    for tone in ['4', '8']:
                        write_dict_line(puj_without_tone, tone, file)
                else:
                    for tone in ['1', '2', '3', '5', '6', '7']:
                        write_dict_line(puj_without_tone, tone, file)


def write_dict_line(puj_without_tone, tone, file):
    puj = f"{puj_without_tone}{tone}"
    line = f"{keyboard_to_handwriting_puj(puj)}\t{simplify_tone(puj)}\n"
    file.write(line)
    line = f"{keyboard_to_handwriting_puj(puj).capitalize()}\t{simplify_tone(puj).capitalize()}\n"
    file.write(line)


if __name__ == "__main__":
    generate_puj_dict("../同音字表-按羅馬字分組.txt","../teochew.dict.yaml")
    pass
