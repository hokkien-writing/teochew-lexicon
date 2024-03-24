#!/usr/bin/python
# -*- coding: UTF-8 -*-
from script.han import Han
from script.puj_list import CombinedPujList


def generate_puj_list(han_list_file, puj_list_file):
    with open(han_list_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        puj_list = []
        for line in lines:
            line = line.strip()
            if line != "":
                character, explanations = line.split(" ", 1)
                han = Han(character, explanations)
                puj_list.extend(han.to_puj_list())
        combined_puj_list = CombinedPujList(puj_list).str_list()
    with open(puj_list_file, 'w', encoding='utf-8') as f:
        f.writelines(combined_puj_list)


if __name__ == '__main__':
    generate_puj_list("../han_list.txt", "../puj_list.txt")
    pass
