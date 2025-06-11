def main():
    book_path = "books/frankenstein.txt"
    book_whole_text = get_book_text(book_path)
    num_words = get_book_num(book_whole_text)
    print(f"{num_words} words found in the document")

def get_book_text(path):
    with open(path) as p:
        return p.read()  
    
from stats import get_book_num

main()
