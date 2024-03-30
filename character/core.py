#!/usr/bin/python
# -*- coding: UTF-8 -*-
import copy
import re

import zhconv

from character.helpers import load_map


class Puj:
    vowel_dict = {
        'a1': 'a', 'a4': 'a', 'a2': 'á', 'a3': 'à', 'a5': 'â', 'a6': 'ã', 'a7': 'ā', 'a8': 'a̍',
        'e1': 'e', 'e4': 'e', 'e2': 'é', 'e3': 'è', 'e5': 'ê', 'e6': 'ẽ', 'e7': 'ē', 'e8': 'e̍',
        'i1': 'i', 'i4': 'i', 'i2': 'í', 'i3': 'ì', 'i5': 'î', 'i6': 'ĩ', 'i7': 'ī', 'i8': 'i̍',
        'o1': 'o', 'o4': 'o', 'o2': 'ó', 'o3': 'ò', 'o5': 'ô', 'o6': 'õ', 'o7': 'ō', 'o8': 'o̍',
        'u1': 'u', 'u4': 'u', 'u2': 'ú', 'u3': 'ù', 'u5': 'û', 'u6': 'ũ', 'u7': 'ū', 'u8': 'u̍',
        'ur1': 'ṳ', 'ur4': 'ṳ', 'ur2': 'ṳ́', 'ur3': 'ṳ̀', 'ur5': 'ṳ̂', 'ur6': 'ṳ̃', 'ur7': 'ṳ̄', 'ur8': 'ṳ̍',
        'n1': 'n', 'n4': 'n', 'n2': 'ń', 'n3': 'ǹ', 'n5': 'n̂', 'n6': 'ñ', 'n7': 'n̄', 'n8': 'n̍',
        'm1': 'm', 'm4': 'm', 'm2': 'ḿ', 'm3': 'm̀', 'm5': 'm̂', 'm6': 'm̃', 'm7': 'm̄',
    }

    def __init__(self, simple_puj, explanations_str=''):
        self.simple_puj = simple_puj
        self.explanations = {}
        if explanations_str != '':
            for exp_str in explanations_str.split():
                exp = Exp(exp_str)
                self.explanations[exp.key] = exp

    def __str__(self):
        exp_strs = []
        for k in self.explanations:
            exp_strs.append(str(self.explanations[k]))
        return f"{self.simple_puj} {' '.join(exp_strs)}".strip()

    def format(self, handwriting=False, with_hans=False):
        exp_str = ""
        for hant in self.explanations:
            exp = self.explanations[hant]
            if with_hans:
                if exp.meaning != '':
                    m = exp.meaning.split(',')[0]
                    mt = m.replace('~', hant)
                    ms = zhconv.convert(mt, 'zh-hans')
                    if ms != mt:
                        for idx, x in enumerate(m):
                            if x == '~':
                                exp.variants.append(ms[idx])
                                break
                else:
                    hans = zhconv.convert(hant, 'zh-hans')
                    if (hans != hant) and (hans not in exp.variants):
                        exp.variants.append(hans)
            exp_str += f"{exp} "
        if handwriting:
            return f"{self.handwriting()} {exp_str}".strip()
        else:
            return f"{self.simple_puj} {exp_str}".strip()

    def keyboard(self):
        _puj = self.simple_puj
        _puj = _puj.replace('1', '')
        _puj = _puj.replace('4', '')
        return _puj

    def handwriting(self):
        _puj = self.simple_puj
        initial, final, tone = self.split()
        # 找到應該標注音調的字母
        # 調值標在音節的韻母之上。或當一個音節有多個字母時：
        # 優先級： a > o > u > e > i。
        # m 作韻腹時標於字母 m 上。
        # 雙字母標於前一個字母上；比如 ng 標示在字母 n 上。
        for c in ['a', 'o', 'ur', 'u', 'e', 'i', 'n', 'm']:
            if final != '' and c in final:
                final = final.replace(c, self.vowel_dict[f"{c}{tone}"])
                _puj = f"{initial}{final}"
                break
            elif final == '' and c in initial:
                initial = initial.replace(c, self.vowel_dict[f"{c}{tone}"])
                _puj = f"{initial}"
                break
        # 替换_puj末尾的nn

        _puj = re.sub(f'nn$', 'ⁿ', _puj)
        _puj = _puj.replace('ur', 'ṳ')
        return _puj

    def split(self):
        _puj = self.simple_puj
        vowels = ["a", "o", "ur", "u", "e", "i", "ng"]
        size = len(_puj)
        if _puj.startswith("ng"):
            return _puj[:2], _puj[2: size - 1], _puj[size - 1]
        for v in vowels:
            pos = _puj.find(v)
            if pos != -1:
                return _puj[:pos], _puj[pos: size - 1], _puj[size - 1]
        return _puj[:size - 1], "", _puj[size - 1]

    def add_explanation(self, character, exp):
        self.explanations[character] = exp


class Exp:
    def __init__(self, explanation_str=''):
        """
        explanation_str: iong3{涌}(~現)
        """
        p1 = ""
        p2 = ""
        p3 = ""

        if "{" in explanation_str:
            p1 = explanation_str.split("{")[0]
        elif "(" in explanation_str:
            p1 = explanation_str.split("(")[0]
        else:
            p1 = explanation_str

        if "{" in explanation_str and "}" in explanation_str:
            p2 = explanation_str.split("{")[1].split("}")[0]

        if "(" in explanation_str and ")" in explanation_str:
            p3 = explanation_str.split("(")[1].split(")")[0]

        self.key = p1
        self.variants = list(p2)
        self.meaning = p3

    def __str__(self):
        exp_str = self.key
        if len(self.variants) > 0:
            exp_str = f"{exp_str}{{{''.join(self.variants)}}}"
        if len(self.meaning) > 0:
            exp_str = f"{exp_str}({self.meaning})"
        return exp_str


class Han:
    def __init__(self, character, explanations_str=''):
        """
        character: 湧
        explanation_str: iong3{涌}(~現) eng2(海~)
        """
        self.character = character
        self.explanations = {}
        if explanations_str != '':
            for exp_str in explanations_str.split():
                exp = Exp(exp_str)
                self.explanations[exp.key] = exp

    def __str__(self):
        exp_strs = []
        for k in self.explanations:
            exp_strs.append(str(self.explanations[k]))
        return f"{self.character} {' '.join(exp_strs)}".strip()

    def to_hans(self):
        """
        Convert the character to simplified Chinese.
        """
        return zhconv.convert(self.character, 'zh-hans')

    def add_explanation(self, puj, comment):
        self.explanations[puj] = comment

    def to_puj_list(self):
        _puj_list = []
        for k in self.explanations:
            _puj = Puj(k)
            exp = copy.copy(self.explanations[k])
            exp.key = self.character
            _puj.add_explanation(self.character, exp)
            _puj_list.append(_puj)
        return _puj_list


class Diepeng:

    def __init__(self, simple_diepeng):
        self.simple_diepeng = simple_diepeng

    def to_puj(self):
        initial_map = load_map("../doc/diepeng_puj_initial_map.txt")
        final_map = load_map("../doc/diepeng_puj_final_map.txt")

        initial, final, tone = self.split_diepeng()
        if initial in initial_map and initial_map[initial] != "":
            initial = initial_map[initial]
        if final in final_map and final_map[final] != "":
            final = final_map[final]
        # Special cases
        if initial == "ts" and (final.startswith('i') or final.startswith('e')):
            initial = "ch"
        if initial == "tsh" and (final.startswith('i') or final.startswith('e')):
            initial = "chh"
        if initial == "z" and (final.startswith('i') or final.startswith('e')):
            initial = "j"
        if (initial not in ['h', ''] and ( \
                        final.startswith('un') or \
                        final.startswith('urn'))) or \
                (final.startswith('ang') or final.startswith('uk')) or \
                (final.startswith('ing') or final.startswith('ik')):
            print(f"Check: {self.simple_diepeng} => {initial}{final}{tone}'")
        return Puj(f"{initial}{final}{tone}")

    def split_diepeng(self):
        """
        Split the Chaozhou pinyin into initial, final, tone
        """
        dp = self.simple_diepeng
        vowels = ["a", "i", "o", "u", "e", "ê"]
        size = len(dp)
        for i, char in enumerate(dp):
            if char in vowels:
                return dp[:i], dp[i: size - 1], dp[size - 1]
        return dp[:size - 1], "", dp[size - 1]


class CombinedPujList:

    def __init__(self, puj_list):
        self.puj_list = puj_list

    def __str__(self):
        return "\n".join(self.str_list())

    def __getitem__(self, item):
        return self.str_list()[item]

    # def format(self, handwriting=False, with_hans=False):
    #     _list = self.combine()
    #     _str_list = []
    #     for item in _list:
    #         _str_list.append(f"{item.format(handwriting, with_hans)}\n")
    #     return _str_list

    def str_list(self):
        _list = self.combine()
        _str_list = []
        for item in _list:
            _str_list.append(f"{item}")
        return _str_list

    def combine(self):
        puj_map = {}
        for puj in self.puj_list:
            if puj.simple_puj in puj_map:
                puj_map[puj.simple_puj].explanations.update(puj.explanations)
            else:
                puj_map[puj.simple_puj] = puj
        _combined_puj_list = []
        for k in sorted(puj_map.keys()):
            _combined_puj_list.append(puj_map[k])
        return _combined_puj_list
