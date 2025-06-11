def get_book_text(book_path):
    with open(book_path) as b:
        book_content = b.read()
        return print(book_content)
    
def main():
    get_book_text("books/frankenstein.txt")

main()
