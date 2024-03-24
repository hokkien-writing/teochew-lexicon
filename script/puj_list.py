#!/usr/bin/python
# -*- coding: UTF-8 -*-
from script.puj import Puj


class CombinedPujList:

    def __init__(self, puj_list):
        self.puj_list = puj_list

    def __str__(self):
        return "".join(self.str_list())

    def format(self, handwriting=False, with_hans=False):
        _list = self.combine()
        _str_list = []
        for item in _list:
            _str_list.append(f"{item.format(handwriting, with_hans)}\n")
        return _str_list

    def str_list(self):
        _list = self.combine()
        _str_list = []
        for item in _list:
            _str_list.append(f"{item}\n")
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


if __name__ == '__main__':
    combined_puj_list = CombinedPujList([
        Puj('hur1', '墟(投～)'),
        Puj('hur1', '墟(投～) 虛(~荣)'),
        Puj('hur1', '噓 圩'),
        Puj('ua2', '我'),
        Puj('ua2', '倚(~樹)'),
    ])
    print(combined_puj_list)
    pass
