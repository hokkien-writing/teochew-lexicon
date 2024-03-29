#!/usr/bin/python
# -*- coding: UTF-8 -*-
from script.common import today
from script.puj import Puj

# 聲母列表
INITIALS = ['', 'p', 'ph', 'b', 'm',
            't', 'th', 'n', 'l',
            'ch', 'chh', 'ts', 'tsh', 's', 'z', 'j',
            'k', 'kh', 'g', 'ng', 'h']
# 韻母列表
FINALS = [
    ['a', 'ah'],
    ['e', 'eh'],
    ['i', 'ih'],
    ['o', 'oh'],
    ['u', 'uh'],
    ['ur', 'urh'],

    ['ia', 'iah'],
    ['ie', 'ieh'],
    ['io', 'ioh'],
    ['iu', 'iuh'],

    ['ua', 'uah'],
    ['ue', 'ueh'],
    ['ui'],

    ['ai', 'aih'],
    ['oi', 'oih'],

    ['uai'],

    ['au', 'auh'],
    ['ou'],

    ['iau', 'iauh'],

    ['ann'],
    ['enn'],
    ['inn'],

    ['iann'],
    ['ienn'],
    ['ionn'],
    ['iunn'],

    ['uann'],
    ['uenn'],
    ['uinn'],

    ['ainn'],
    ['oinn'],

    ['uainn'],

    ['aunn'],
    ['ounn'],

    ['iaunn'],

    ['an', 'at'],
    ['in', 'it'],
    ['un', 'ut'],
    ['urn', 'urt'],

    ['ian', 'iat'],
    ['uan', 'uat'],

    ['am', 'ap'],
    ['om'],
    ['im', 'ip'],

    ['iam', 'iap'],
    ['uam', 'uap'],

    ['ang', 'ak'],
    ['eng', 'ek'],
    ['ing', 'ik'],
    ['ong', 'ok'],
    ['ung', 'uk'],

    ['iang', 'iak'],
    ['iong', 'iok'],

    ['uang', 'uak'],

    ['m'],
    ['ng', 'ngh'],
]

# 聲調標識
CIRCLED_NUMBERS = ["⓪", "①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨"]


def generate_puj_table(puj_list_file, puj_table_file):
    puj_map = {}
    with open(puj_list_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line != "":
                simple_puj, explanations = line.split(" ", 1)
                puj = Puj(simple_puj, explanations)
                puj_map[simple_puj] = puj
    with open(puj_table_file, 'w', encoding='utf-8') as f:
        f.writelines(f'''---
title: "潮汕話同音字表 v{today()}"
author: "github.com/tsunhua/teochew-character"
keywords: ["潮汕話","潮州話","白話字"]
---

''')
        # Iterate over each final
        for final in FINALS:
            title = ""
            if len(final) > 1:
                title = f"{Puj(final[0] + '1').handwriting()} / {Puj(final[1] + '1').handwriting()}"
            else:
                title = f"{Puj(final[0] + '1').handwriting()}"
            print(f"{title}")
            write_title = False
            # Iterate over each initial
            for initial in INITIALS:
                # Combine initial with final and digits 1-8
                write_sh = False
                for digit in range(1, 9):
                    if digit in [4, 8] and len(final) > 1:
                        simple_puj = final[1] + str(digit)
                    else:
                        simple_puj = final[0] + str(digit)
                    if initial != '':
                        simple_puj = initial + simple_puj
                    if simple_puj in puj_map:
                        if not write_title:
                            f.write(f"## {title}\n\n")
                            f.write(f"| |{title}|\n")
                            f.write(f"|-|----|\n")
                            write_title = True
                        if not write_sh:
                            if initial == "":
                                f.write(f"| |")
                            else:
                                f.write(f"|{initial}|")
                            write_sh = True
                        puj = puj_map[simple_puj]
                        f.write(f" {map_to_circled_numbers(digit)} {puj.format(handwriting=True, with_hans=True)}  ")
                if write_sh:
                    f.write("|\n")
            print()  # Print an extra newline after each final
            if write_title:
                f.write("\n")
    print("生成同音字表完畢！")


def map_to_circled_numbers(number):
    return CIRCLED_NUMBERS[number] if 0 <= number <= 9 else f"无效输入：{number}"


if __name__ == '__main__':
    generate_puj_table("../puj_list.txt", "../puj_table.md")
    pass
