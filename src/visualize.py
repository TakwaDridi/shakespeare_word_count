def show_top_n_words(word_count: dict,
                     n: int = 10):
    """
    :param word_count: dictionary containing words as its keys and their respective
     number of occurrences as its values
    :param n: number of words to print
    :return:
    """
    word_count = list(zip(word_count.keys(), word_count.values()))

    word_count = sorted(word_count,
                        key=lambda x: x[1],
                        reverse=True)

    for i, (word, n_occ) in enumerate(iterable=word_count, start=1):
        print(word, f'({n_occ})')
        if i >= n:
            break
