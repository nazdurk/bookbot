from stats import get_num_words, get_dict, sorted_count, get_book_text
import sys
#get_book_text()
def main():
    my_chars_data = sorted_count()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print((f"Found {get_num_words()} total words"))
    print("--------- Character Count -------")
    for item_dict in my_chars_data:
        print(f"{item_dict['char']}: {item_dict['num']}")
    print("============= END ===============")
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()