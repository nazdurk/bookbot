from stats import get_num_words, get_dict, sorted_count, get_book_text
#get_book_text()
def main():
    my_chars_data = sorted_count()
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print((f"Found {get_num_words()} total words"))
    print("--------- Character Count -------")
    for item_dict in my_chars_data:
        print(f"{item_dict['char']}: {item_dict['num']}")
    print("============= END ===============")
main()