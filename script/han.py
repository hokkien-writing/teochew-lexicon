from zhconv import convert


def read_first_character(filename):
    """Read the file and return the first Chinese character of each line."""
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip()[0] for line in f]


def find_unique_characters(file1, file2):
    """Find the characters in file1 that are not in file2."""
    characters1 = set(read_first_character(file1))
    characters2 = set(read_first_character(file2))
    unique_characters = characters1 - characters2
    return sorted(list(unique_characters))


def find_duplicate(file_path):
    """Find duplicate characters in the file."""
    characters_map = {}
    duplicate_characters = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            character = line.strip()[0]
            if character in characters_map:
                duplicate_characters.append(character)
            else:
                characters_map[character] = character
    return sorted(duplicate_characters)


def first_character_in_line_to_hant(file_path):
    """Convert the first character of each line in the file to traditional Chinese."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    result = ""
    for line in lines:
        char = line.strip()[0]
        traditional_char = convert(char, 'zh-hant')
        if char != traditional_char:
            result += f"{traditional_char}{line[1:]}"
        else:
            result += line
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(result)


def to_hant(input_file_path, output_file_path):
    """
    Convert the characters in the input document to traditional Chinese and save the result to the output file
    """
    # Read the input document containing mixed characters
    with open(input_file_path, "r", encoding="utf-8") as file:
        document_content = file.read()

    # Initialize the result string
    result = ""

    # Process each character in the document
    for char in document_content:
        # Convert the character to traditional Chinese
        traditional_char = convert(char, 'zh-hant')

        # If the character has a corresponding traditional character, add it with parentheses
        if char != traditional_char:
            result += f"{traditional_char}[{char}]"
        else:
            # Otherwise, keep the original character
            result += char

    # Write the result to an output file
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(result)

    print(f"Processing complete. Result saved to {output_file_path}")
    return output_file_path
