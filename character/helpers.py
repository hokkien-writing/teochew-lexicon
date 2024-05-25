from datetime import datetime

superscript_mapping = {
    "⁰": "0",
    "¹": "1",
    "²": "2",
    "³": "3",
    "⁴": "4",
    "⁵": "5",
    "⁶": "6",
    "⁷": "7",
    "⁸": "8",
    "⁹": "9",
}


def today():
    # Get current date
    current_date = datetime.now()
    # Format date
    return current_date.strftime("%Y.%m.%d")


def load_map(file_path):
    my_map = {}
    with open(file_path, "r") as f:
        for line in f:
            if " " in line:
                k, v = line.strip().split()
                my_map[k] = v
    return my_map


def read_first_character(filename):
    """Read the file and return the first Chinese character of each line."""
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip()[0] for line in f]


def replace_superscript(superscript_str):
    for superscript in superscript_mapping:
        superscript_str = str(superscript_str).replace(superscript, superscript_mapping[superscript])
    return superscript_str
