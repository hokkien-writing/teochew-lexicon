from zhconv import convert

# 聲母列表
INITIALS = ['', 'p', 'ph', 'b', 'm',
            't', 'th', 'n', 'l',
            'ch', 'chh', 'ts', 'tsh', 's', 'z', 'j',
            'k', 'kh', 'g', 'ng', 'h']
# 韻母列表
FINALS = [
    ['a', 'ah'],
    ['e', 'eh'],
    ['i', 'ih'],
    ['o', 'oh'],
    ['u', 'uh'],
    ['ṳ', 'ṳh'],

    ['ia', 'iah'],
    ['ie', 'ieh'],
    ['io', 'ioh'],
    ['iu', 'iuh'],

    ['ua', 'uah'],
    ['ue', 'ueh'],
    ['ui'],

    ['ai', 'aih'],
    ['oi', 'oih'],

    ['uai'],

    ['au', 'auh'],
    ['ou'],

    ['iau', 'iauh'],

    ['aⁿ'],
    ['eⁿ'],
    ['iⁿ'],

    ['iaⁿ'],
    ['ieⁿ'],
    ['ioⁿ'],
    ['iuⁿ'],

    ['uaⁿ'],
    ['ueⁿ'],
    ['uiⁿ'],

    ['aiⁿ'],
    ['oiⁿ'],

    ['uaiⁿ'],

    ['auⁿ'],
    ['ouⁿ'],

    ['iauⁿ'],

    ['an', 'at'],
    ['in', 'it'],
    ['un', 'ut'],
    ['ṳn', 'ṳt'],

    ['ian', 'iat'],
    ['uan', 'uat'],

    ['am', 'ap'],
    ['om'],
    ['im', 'ip'],

    ['iam', 'iap'],
    ['uam', 'uap'],

    ['ang', 'ak'],
    ['eng', 'ek'],
    ['ing', 'ik'],
    ['ong', 'ok'],
    ['ung', 'uk'],

    ['iang', 'iak'],
    ['iong', 'iok'],

    ['uang', 'uak'],

    ['m'],
    ['ng', 'ngh'],
]

# 聲調標識
CIRCLED_NUMBERS = ["⓪", "①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨"]


# Functions
def map_to_circled_numbers(number):
    return CIRCLED_NUMBERS[number] if 0 <= number <= 9 else f"无效输入：{number}"


# 同音字表
def generate_homophone_table(input_file_path, output_file_path):
    pinyin_to_characters = {}

    # Read the input file and populate the dictionary
    with open(input_file_path, 'r') as file:
        for line in file:
            line = line.strip().lower()
            if line:
                pinyin, *characters = line.split()
                result = ""
                for char in characters:
                    simp_char = convert(char, 'zh-hans')
                    if char != simp_char:
                        result += f"{char}[{simp_char}]"
                    else:
                        # Otherwise, keep the original character
                        result += char
                pinyin_to_characters[pinyin] = result

    # Initialize the output file
    with open(output_file_path, 'w') as file:
        # Iterate over each yun
        for yun in FINALS:
            title = ""
            if len(yun) > 1:
                title = f"{yun[0]} / {yun[1]}"
            else:
                title = f"{yun[0]}"
            print(f"{title}")
            write_title = False
            # Iterate over each sheng
            for sh in INITIALS:
                # Combine sheng with yun and digits 1-8
                write_sh = False
                for digit in range(1, 9):
                    if digit in [4, 8] and len(yun) > 1:
                        pinyin = yun[1] + str(digit)
                    else:
                        pinyin = yun[0] + str(digit)
                    if sh != '':
                        pinyin = sh + pinyin
                    if pinyin in pinyin_to_characters:
                        if not write_title:
                            file.write(f"## {title}\n\n")
                            file.write(f"| |{title}|\n")
                            file.write(f"|-|----|\n")
                            write_title = True
                        if not write_sh:
                            file.write(f"|{sh}|")
                            write_sh = True
                        characters = pinyin_to_characters[pinyin]
                        print(f"{pinyin} {' '.join(characters)}")
                        file.write(f" {map_to_circled_numbers(digit)}{''.join(characters)}")
                        file.write(" ")
                if write_sh:
                    file.write("|\n")
            print()  # Print an extra newline after each yun
            if write_title:
                file.write("\n")
    print("生成同音字表完畢！")
    return output_file_path


def generate_character_roman_dict(character_roman_file):
    character_roman_dict = {}
    with open(character_roman_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split()
                character = parts[0]
                romans = parts[1:]
                character_roman_dict[character] = romans
    return character_roman_dict


def generate_homophone_list(character_roman_file, output_file):
    chinese_pinyin_dict = generate_character_roman_dict(character_roman_file)
    homophone_dict = {}
    for chinese_word, pinyin_list in chinese_pinyin_dict.items():
        for pinyin in pinyin_list:
            if pinyin not in homophone_dict:
                homophone_dict[pinyin] = []
            homophone_dict[pinyin].append(chinese_word)
    sorted_homophone_dict = dict(sorted(homophone_dict.items()))
    with open(output_file, 'w', encoding='utf-8') as file:
        for pinyin, words in sorted_homophone_dict.items():
            file.write(f"{pinyin} {' '.join(words)}\n")
    print(f"生成完畢！")
    return output_file


def merge(character_roman_file, amend_file, out_file):
    amend_dict = {}
    with open(amend_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split()
                character = parts[0]
                amend_dict[character] = line

    result = []
    with open(character_roman_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split()
                character = parts[0]
                if line in result:
                    continue
                if character in amend_dict:
                    result.append(amend_dict[character])
                else:
                    result.append(line)
    with open(out_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(result))
