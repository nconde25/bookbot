def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sort_list = sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} found in this document\n")

    for x in sort_list:
        if x["char"].isalpha():
            print(f"The {x["char"]} character was found {x["num"]} times")

    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()     
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def sorted_list(dict):
    sorted_list = []
    for letter in dict:
        sorted_list.append({"char": letter, "num": dict[letter]})
        sorted_list.sort(key=sort_on,reverse=True)
    return sorted_list



main()