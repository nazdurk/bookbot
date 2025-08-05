def get_num_words():
    with open("books/frankenstein.txt") as my_file:
        data = my_file.read()
        num_words = len(data.split())
    return num_words

def get_dict():
    with open("books/frankenstein.txt") as my_file:
        data = my_file.read()
    my_dict = {}
    for i in data:
        if i.lower() in my_dict:
            my_dict[i.lower()] += 1
        else:
            my_dict[i.lower()] = 1
    return my_dict

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
    sorted_list = sorted(my_dict.items(),reverse=True, key=lambda x:x[1])
    new_list = []
    for k, v in sorted_list:
        new_list.append({"char": k, "num": v})
    return new_list

def get_book_text():
    with open("books/frankenstein.txt") as f:
        book_contents = f.read()
        print(book_contents)