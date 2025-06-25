def get_num_words():
    with open("books/frankenstein.txt") as my_file:
        data = my_file.read()
        num_words = len(data.split())
    print(f"{num_words} words found in the document")

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