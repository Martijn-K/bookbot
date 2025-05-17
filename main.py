import sys

from stats import get_num_words, count_unique_chars, sort_list_of_dictionaries

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # start reading the book
        file_contents = f.read()
        return file_contents

def printer(path_to_book, nr_of_words, sorted_chars):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path_to_book}...\n----------- Word Count ----------\nFound {nr_of_words} total words\n--------- Character Count -------")
    for char in sorted_chars:
        print(f"{char["char"]}: {char["num"]}")
    print(f"============= END ===============")

def  main():
    args = sys.argv[1:]
    if len(args) < 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = args[0]
    book_contents = get_book_text(path_to_book)
    nr_of_words, _ = get_num_words(book_contents)

    print(f"{nr_of_words} words found in the document")
    unique_chars = count_unique_chars(book_contents)


    sorted_chars = sort_list_of_dictionaries(unique_chars)
    printer(path_to_book, nr_of_words, sorted_chars)
    


main()
