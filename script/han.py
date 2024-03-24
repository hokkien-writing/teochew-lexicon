#!/usr/bin/python
# -*- coding: UTF-8 -*-
import zhconv

from script.common import convert_to_explanation_map
from script.puj import Puj


class Han:
    def __init__(self, character, explanation_str=''):
        self.character = character
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
        return f"{self.character} {exp}".strip()

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
            _puj.add_explanation(self.character, self.explanations[k])
            _puj_list.append(_puj)
        return _puj_list


if __name__ == '__main__':
    hanjit = Han("尻", "khau1 ka1(~倉)")
    print(hanjit)
    puj_list = hanjit.to_puj_list()
    for puj in puj_list:
        print(f"{puj.simple_puj} {puj.explanations}")
    pass
