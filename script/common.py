from datetime import datetime


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


def convert_to_explanation_map(explanation_str):
    explanation_map = {}
    for explanation in explanation_str.split():
        if '(' in explanation:
            key, comment = explanation.split('(')
            comment = comment[:-1]
            explanation_map[key] = comment
        else:
            explanation_map[explanation] = ""
    return explanation_map


def read_first_character(filename):
    """Read the file and return the first Chinese character of each line."""
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip()[0] for line in f]
