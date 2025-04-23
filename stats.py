def get_word_count(file_contents):
    num_words = len(file_contents.split())
    print(f"{num_words} words found in the document")
    return num_words

def get_character_counts(file_contents):
    file_contents = file_contents.lower()
    all_chars = set()
    for char in file_contents:
        all_chars.add(char)
    all_chars_dict = {}
    for char in all_chars:
        counter = 0
        for i in range(0, len(file_contents)):
            if file_contents[i] == char: 
                counter += 1
        all_chars_dict.update({char : counter})
    return all_chars_dict

def sort_on(dict):
    return dict["num"]

def sort_char_counts(all_chars_dict):
    new_list = []
    for key in all_chars_dict:
        if key.isalpha():
            new_list.append({"char": key, "num": all_chars_dict[key]})
    new_list.sort(reverse=True, key=sort_on)

    return new_list

