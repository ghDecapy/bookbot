def main():
    book_path = "books/frankenstein.txt"
    book_whole_text = get_book_text(book_path)
    num_words = get_book_num(book_whole_text)
    print(f"{num_words} words found in the document")

def get_book_text(path):
    with open(path) as p:
        return p.read()
    
def get_book_num(book_text):
    book_words_list = book_text.split()
    return len(book_words_list)
    

main()
