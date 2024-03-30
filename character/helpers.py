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


def read_first_character(filename):
    """Read the file and return the first Chinese character of each line."""
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip()[0] for line in f]
