import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    book_whole_text = get_book_text(book_path)
    num_words = get_book_num(book_whole_text)
    character_count = counting_characters(book_whole_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    report_formatting(character_count)
    print("============= END ===============")

def get_book_text(path):
    with open(path) as p:
        return p.read()  
    
from stats import get_book_num, counting_characters, sort_by, sorting_characters, report_formatting

main()
