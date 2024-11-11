# with open("./books/frankenstein.txt", 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line)
import string

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict['num']

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char" : ch, "num" : num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    #print(num_words)
    chars_dict = count_chars(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    # print(f"--- Begin report of books/frankenstein.txt ---\n{num_words} words found in the document")
    # for char in chars_dict.keys():
    #     print(f"The '{char}' character was found {chars_dict[char]} times\n")
    # print("--- End report ---")

if __name__ == "__main__":
    main()