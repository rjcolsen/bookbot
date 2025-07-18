# with open("/home/work/bookbot/books/frankenstein.txt") as f:
#     book_text = f.read()

def text_count(book_text):
    words = 0
    book_words = book_text.split()
    for word in book_words:
        words = words + 1
    return words
    
def char_count(book_text):
    chars = {}
    book_lower = book_text.lower()
    for letter in book_lower:
        if letter in chars:
            chars[letter] += 1
        elif letter not in chars:
            chars[letter] = 1
    return chars

def sort_on(chars):
    return chars["num"]

def sort_results(chars):
    sorted = []
    cleaned = ""
    for item in chars:
        new_entry = {"char": item, "num": chars[item]}
        if new_entry["char"].isalpha():
            sorted.append(new_entry)
    sorted.sort(reverse=True, key=sort_on)
    # return sorted
    for letter in sorted:
        a = letter["char"]
        b = letter["num"]
        cleaned += (f"{a}: {b}\n")
    return cleaned[:-1]

# text_count(book_text)
# char_count(book_text)