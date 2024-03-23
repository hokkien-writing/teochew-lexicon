from script.han_dict_generator import generate_han_dict
from script.homophone_table import generate_homophone_list
from script.homophone_table import generate_homophone_table
from script.puj_dict_generator import generate_puj_dict

if __name__ == '__main__':
    generate_homophone_list("常用漢字-羅馬字.txt",
                            "同音字表-按羅馬字分組.txt")
    generate_homophone_table("同音字表-按羅馬字分組.txt",
                             "同音字表-按韻母分組.md")
    generate_han_dict("同音字表-按羅馬字分組.txt",
                      "teochew.han.dict.yaml")
    generate_puj_dict("同音字表-按羅馬字分組.txt",
                      "teochew.puj.dict.yaml")
