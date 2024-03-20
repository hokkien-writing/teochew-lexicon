def split_chaopin(pinyin):
    """
    Split the Chaozhou pinyin into sheng, yun, and diao
    """
    vowels = ["a", "i", "o", "u", "e", "ê"]
    size = len(pinyin)
    for i, char in enumerate(pinyin):
        if char in vowels:
            return pinyin[:i], pinyin[i: size - 1], pinyin[size - 1]
    return pinyin[:size - 1], "", pinyin[size - 1]


def convert_chaopin_to_roman(input_file, output_file):
    """
    Convert the Chaozhou pinyin to romanized pinyin, and write the result to the output file
    """
    # Load the mappings
    yun_map = load_file_to_map("doc/潮拼-羅馬字韻母.txt")
    sheng_map = load_file_to_map("doc/潮拼-羅馬字聲母.txt")

    # Read the input file
    with open(input_file, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    converted_lines = []
    todo_lines = []

    for line in lines:
        # Extract the Chinese character and the Chaozhou pinyin
        chinese_char, pinyins = line.strip().split(" ", 1)

        new_pinyins = []
        todo = False
        for pinyin in pinyins.strip().split():
            # Extract the sheng, yun, and diao
            sheng, yun, diao = split_chaopin(pinyin)
            # Replace the sheng and yun with the corresponding romanized pinyin
            if sheng in sheng_map and sheng_map[sheng] != "":
                sheng = sheng_map[sheng]
            if yun in yun_map and yun_map[yun] != "":
                yun = yun_map[yun]
            # Special cases
            if sheng == "ts" and (yun.startswith('i') or yun.startswith('e')):
                sheng = "ch"
            if sheng == "tsh" and (yun.startswith('i') or yun.startswith('e')):
                sheng = "chh"
            if sheng == "z" and (yun.startswith('i') or yun.startswith('e')):
                sheng = "j"
            if (sheng not in ['h', ''] and ( \
                            yun.startswith('un') or \
                            yun.startswith('ṳn'))) or \
                    (yun.startswith('ang') or yun.startswith('uk')) or \
                    (yun.startswith('ing') or yun.startswith('ik')):
                todo = True
            new_pinyins.append(f"{sheng}{yun}{diao}")
        converted_lines.append(f"{chinese_char} {' '.join(new_pinyins)}")
        if todo:
            todo_lines.append(f"{chinese_char} {' '.join(new_pinyins)}")

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("\n".join(converted_lines))

    with open(f"{output_file}.todo", "w", encoding="utf-8") as file:
        file.write("\n".join(todo_lines))

    print("轉換完畢！")

def load_file_to_map(file_path):
    my_map = {}
    with open(file_path, "r") as f:
        for line in f:
            if " " in line:
                k, v = line.strip().split()
                my_map[k] = v
    return my_map
