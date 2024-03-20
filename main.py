from script.han import first_character_in_line_to_hant
from script.roman import convert_chaopin_to_roman
from script.homophone_table import generate_homophone_list
from script.homophone_table import generate_homophone_table
from script.homophone_table import merge

if __name__ == '__main__':
    # first_character_in_line_to_hant("doc/常用漢字-潮拼.txt")
    # convert_chaopin_to_roman("doc/常用漢字-潮拼.txt","doc/常用漢字-羅馬字.txt")
    # merge("doc/常用漢字-羅馬字.txt",
    #       'doc/常用漢字-羅馬字-修補.txt',
    #       "常用漢字-羅馬字.txt")
    generate_homophone_list("常用漢字-羅馬字.txt",
                            "同音字表-按羅馬字分組.txt")
    generate_homophone_table("同音字表-按羅馬字分組.txt",
                             "同音字表-按韻母分組.md")
