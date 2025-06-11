def get_book_num(book_text):
    book_words_list = book_text.split()
    return len(book_words_list)

def counting_characters(book_text):
    char_list = {}
    lc_string = book_text.lower()
    for char in lc_string:
        if char in char_list:
            char_list[char] += 1
        else:
            char_list[char] = 1
    return char_list
