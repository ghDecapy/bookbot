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

def sort_by(char_list):
    return char_list["num"]

def sorting_characters(char_list):
    letters_list = []
    for char, count in char_list.items():
        if char.isalpha() == True:
            letters_list.append({"char": char, "num": count})
        letters_list.sort(reverse=True, key=sort_by)
    return letters_list

def report_formatting(char_list):
    sorted_list = sorting_characters(char_list)
    for char in sorted_list:
        print(f"{char["char"]}:", char["num"])
