#!/usr/bin/python
# -*- coding: UTF-8 -*-
from script.common import load_map
from script.puj import Puj


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


if __name__ == '__main__':
    dp = Diepeng('diê5')
    print(dp.to_puj().simple_puj)
    dp = Diepeng('ziu1')
    print(dp.to_puj().simple_puj)
