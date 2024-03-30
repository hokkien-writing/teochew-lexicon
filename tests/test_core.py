import unittest

from character.core import Han, Puj, Exp, Diepeng, CombinedPujList


class TestCore(unittest.TestCase):
    def test_han(self):
        hanjit = Han("尻", "khau1 ka1(~倉)")
        self.assertEqual("尻 khau1 ka1(~倉)", str(hanjit))
        puj_list = hanjit.to_puj_list()
        self.assertEqual("khau1", puj_list[0].simple_puj)
        self.assertEqual("尻", str(puj_list[0].explanations['尻']))
        self.assertEqual("ka1", puj_list[1].simple_puj)
        self.assertEqual("尻(~倉)", str(puj_list[1].explanations['尻']))

        hanjit = Han("湧", "iong3{涌}(~現) eng2(海~)")
        self.assertEqual("湧 iong3{涌}(~現) eng2(海~)", str(hanjit))
        puj_list = hanjit.to_puj_list()
        self.assertEqual("iong3", puj_list[0].simple_puj)
        self.assertEqual("湧{涌}(~現)", str(puj_list[0].explanations['湧']))
        self.assertEqual("eng2", puj_list[1].simple_puj)
        self.assertEqual("湧(海~)", str(puj_list[1].explanations['湧']))

    def test_puj(self):
        puj = Puj('hur1', '墟(投～) 虛(~荣) 噓 圩')
        self.assertEqual("hur1 墟(投～) 虛(~荣) 噓 圩", str(puj))
        self.assertEqual("hṳ", puj.handwriting())
        puj = Puj('m6')
        self.assertEqual("m̃", puj.handwriting())
        puj = Puj('nng7')
        self.assertEqual("nn̄g", puj.handwriting())
        puj = Puj('nguan6')
        self.assertEqual("nguãn", puj.handwriting())
        puj = Puj('ngur2')
        self.assertEqual("ngṳ́", puj.handwriting())
        puj = Puj('mng5')
        self.assertEqual("mn̂g", puj.handwriting())
        puj = Puj('Thoin5')
        self.assertEqual("Thôin", puj.handwriting())
        puj = Puj('Tsui3')
        self.assertEqual("Tsùi", puj.handwriting())
        puj = Puj('sio5')
        self.assertEqual("siô", puj.handwriting())

    def test_diepeng(self):
        dp = Diepeng('diê5')
        self.assertEqual("tie5", dp.to_puj().simple_puj)
        dp = Diepeng('ziu1')
        self.assertEqual("chiu1", dp.to_puj().simple_puj)

    def test_exp(self):
        exp = Exp("iong3{涌}(~現)")
        self.assertEqual("iong3{涌}(~現)", str(exp))
        exp = Exp("iong3(~現)")
        self.assertEqual("iong3(~現)", str(exp))
        exp = Exp("iong3")
        self.assertEqual("iong3", str(exp))

    def test_combined_puj_list(self):
        combined_puj_list = CombinedPujList([
            Puj('hur1', '墟(投～)'),
            Puj('hur1', '墟(投～) 虛(~荣)'),
            Puj('hur1', '噓 圩'),
            Puj('ua2', '我'),
            Puj('ua2', '倚(~樹)'),
        ])
        self.assertEqual("hur1 墟(投～) 虛(~荣) 噓 圩", str(combined_puj_list[0]))
        self.assertEqual("ua2 我 倚(~樹)", str(combined_puj_list[1]))


if __name__ == '__main__':
    unittest.main()
