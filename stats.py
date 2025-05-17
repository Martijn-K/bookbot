def get_num_words(book_text):
    total_wordcount = 0
    total_words = []
    lines = book_text.splitlines()
    for line in lines:
        words = line.split()
        total_words += words
        wordcount = len(words)
        total_wordcount += wordcount
    return total_wordcount, total_words

def count_unique_chars(book_text):
    chars = {}
    _, words = get_num_words(book_text)
    for word in words:
        characters = word.lower()
        for char in characters:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars


def sort_list_of_dictionaries(dict_in):
    list_of_dicts = []
    
    for key in dict_in:
        new_dict = {"char": key, "num": dict_in[key]}
        list_of_dicts.append(new_dict)

    # “For each dictionary d in the list, use d["count"] as the sorting key.”
    list_of_dicts.sort(key=lambda d: d["num"], reverse=True)

    return list_of_dicts