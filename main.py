from stats import get_word_count
from stats import get_character_counts
from stats import sort_char_counts
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    file = ""
    if len(sys.argv) == 2:
        file = str(sys.argv[1])
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    word_count = get_word_count((get_book_text(file)))
    char_dict = get_character_counts(get_book_text(file))
    char_list = sort_char_counts(char_dict)
    print(f'''============ BOOKBOT ============
Analyzing book found at {file}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------''')


    for i in range(0, len(char_list)):
        print(f"{char_list[i]["char"]}: {char_list[i]["num"]}")

    print("============= END ===============")


main()
