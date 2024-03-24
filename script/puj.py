#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

import zhconv

from script.common import convert_to_explanation_map


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

    def __init__(self, simple_puj, explanation_str=''):
        self.simple_puj = simple_puj
        if explanation_str != '':
            self.explanations = convert_to_explanation_map(explanation_str)
        else:
            self.explanations = {}

    def __str__(self):
        exp = ""
        for k in self.explanations:
            v = self.explanations[k]
            if v != "":
                exp += f"{k}({v}) "
            else:
                exp += f"{k} "
        return f"{self.simple_puj} {exp}".strip()

    def format(self, handwriting=False, with_hans=False):
        exp = ""
        for k in self.explanations:
            v = self.explanations[k]
            key = k
            if with_hans:
                hans = zhconv.convert(k, 'zh-hans')
                if hans != k:
                    key = f"{k}{{{hans}}}"
            if v != "":
                exp += f"{key}({v}) "
            else:
                exp += f"{key} "
        if handwriting:
            return f"{self.handwriting()} {exp}".strip()
        else:
            return f"{self.simple_puj} {exp}".strip()

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

    def add_explanation(self, character, comment):
        self.explanations[character] = comment


if __name__ == '__main__':
    puj = Puj('hur1', '墟(投～) 虛(~荣) 噓 圩')
    print(puj)
    print(puj.handwriting())
    puj = Puj('m6')
    print(puj.handwriting())
    puj = Puj('nng7')
    print(puj.handwriting())
    puj = Puj('nguan6')
    print(puj.handwriting())
    puj = Puj('ngur2')
    print(puj.handwriting())
    puj = Puj('mng5')
    print(puj.handwriting())
    puj = Puj('Thoin5')
    print(puj.handwriting())
    puj = Puj('Tsui3')
    print(puj.handwriting())
    puj = Puj('sio5')
    print(puj.handwriting())
    pass
