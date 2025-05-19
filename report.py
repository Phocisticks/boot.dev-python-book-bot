def print_character_dict(c_dict):
    for c in c_dict:
        if c.isalpha():
            print(f"{c}: {c_dict[c]}")

def print_report(file_path, word_count, c_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print_character_dict(c_dict)