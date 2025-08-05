def get_num_words():
    with open("books/frankenstein.txt") as my_file:
        data = my_file.read()
        num_words = len(data.split())
    print(f"Found {num_words} total words")

def get_dict():
    with open("books/frankenstein.txt") as my_file:
        data = my_file.read()
    my_dict = {}
    for i in data:
        if i.lower() in my_dict:
            my_dict[i.lower()] += 1
        else:
            my_dict[i.lower()] = 1
    print(my_dict)

def sorted_count():
    with open("books/frankenstein.txt") as my_file:
        data = my_file.read()
    my_dict = {}
    for i in data:
        if i.isalpha():
            if i.lower() in my_dict:
                my_dict[i.lower()] += 1
            else:
                my_dict[i.lower()] = 1
    sorted_dict = sorted(my_dict.items(),reverse=True, key=lambda x:x[1])
    for k, v in sorted_dict:
        print(f"{k}: {v}")

def get_book_text():
    with open("books/frankenstein.txt") as f:
        book_contents = f.read()
        print(book_contents)