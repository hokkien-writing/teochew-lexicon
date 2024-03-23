from datetime import datetime

# 單韻母
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

# swapped_vowel_dict = {value: key for key, value in vowel_dict.items()}

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


def to_keyboard_vowel(puj):
    puj = puj.replace('ⁿ', 'nn')
    puj = puj.replace('ṳ', 'ur')
    return puj


def to_handwriting_vowel(puj):
    puj = puj.replace('nn', 'ⁿ')
    puj = puj.replace('ur', 'ṳ')
    return puj


def simplify_tone(puj):
    puj = puj.replace('1', '')
    puj = puj.replace('4', '')
    return puj


def to_keyboard_puj(puj):
    puj = simplify_tone(puj)
    puj = to_keyboard_vowel(puj)
    return puj


def keyboard_to_handwriting_puj(puj):
    initial, final, tone = split_keyboard_puj(puj)
    # 找到應該標注音調的字母
    # 调值标在音节的韵母之上。或当一个音节有多个字母时：
    # 优先级： a > o > u > e > i。
    # m 作韵腹时标于字母 m 上。
    # 双字母标于前一个字母上；比如 ng 标示在字母 n 上。
    for c in ['a', 'o', 'u', 'e', 'i', 'm', 'n']:
        if c in final:
            final = final.replace(c, vowel_dict[f"{c}{tone}"])
            puj = f"{initial}{final}"
            break

    puj = puj.replace('nn', 'ⁿ')
    puj = puj.replace('ur', 'ṳ')
    return puj


def split_keyboard_puj(keyboard_puj):
    vowels = ["a", "i", "o", "u", "e"]
    size = len(keyboard_puj)
    for i, char in enumerate(keyboard_puj):
        if char in vowels:
            return keyboard_puj[:i], keyboard_puj[i: size - 1], keyboard_puj[size - 1]
    return keyboard_puj[:size - 1], "", keyboard_puj[size - 1]


def today():
    # Get current date
    current_date = datetime.now()
    # Format date
    return current_date.strftime("%Y.%m.%d")
