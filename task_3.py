def count_word(file_path: str, needed_word: str) -> int:
    """
    Counts number of giver word occurrences in the text file
    :param file_path: path to the file
    :param needed_word: word to count
    :return: number of word occurrences
    """

    # TODO: if the usage model is using straightforward approach considering one big text and one word.
    #  Depending on the desired use case, it may not be the optimal solution, i.e.:
    #  - Counting different words many times against the same text
    #  - Counting same "big" word against multiple texts
    #  - Considering fuzzy search (trying to fix typos)
    instances = 0
    with open(file_path, 'r') as f:
        # TODO: we're considering EOL as word separator as well,
        #  which may not be the case in specific conditions i.e.
        #  when input is a hyphenated text
        for line in f:
            # Splitting string by whitespaces, assuming this is a normal word separator
            # TODO: check whether other symbols are also considered separators
            for word in line.split():
                # TODO: considering word as atomic, so not checking for substrings
                #  i.e. word "a" won't be found in text "aa aaa aa"
                if word == needed_word:
                    instances += 1
    return instances


if __name__ == '__main__':
    print(count_word('task_3_input.txt', 'third'))
