def show_top_n_words(word_count: dict,
                     n: int = 10) -> None:
    """
    This function prints the top-n occurring words in the word_count dictionary.

    :param word_count: dictionary containing words as its keys and their respective
     number of occurrences as its values
    :param n: number of words to print
    """
    word_count = list(zip(word_count.keys(), word_count.values()))

    word_count = sorted(word_count,
                        key=lambda x: x[1],
                        reverse=True)

    for i, (word, n_occ) in enumerate(iterable=word_count, start=1):
        print(f'{word:10}', f'({n_occ})')
        if i >= n:
            break
