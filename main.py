import sys
from stats import count_words, count_characters, order_dictionary_by_count
from report import print_report


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    count = count_words(text)
    character_count = count_characters(text)
    character_count = order_dictionary_by_count(character_count)
    
    print_report(file_path, count, character_count)

main()