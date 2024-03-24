from script.han_dict_generator import generate_han_dict
from script.puj_dict_generator import generate_puj_dict
from script.puj_list_generator import generate_puj_list
from script.puj_table_generator import generate_puj_table

if __name__ == '__main__':
    generate_puj_list("han_list.txt", "puj_list.txt")
    generate_puj_table("puj_list.txt", "puj_table.md")
    generate_han_dict("puj_list.txt", "teochew.han.dict.yaml")
    generate_puj_dict("puj_list.txt", "teochew.puj.dict.yaml")
