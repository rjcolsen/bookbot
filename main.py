# print("time to start being a programmer")
import sys
from stats import text_count
from stats import char_count
from stats import sort_results

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path = sys.argv[1]

with open(path) as f:
    book_text = f.read()

word_count = text_count(book_text)
char_count = char_count(book_text)
sorted = sort_results(char_count)

def main():
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {word_count} total words\n--------- Character Count -------\n{sorted}\n============= END ===============")
    
main()