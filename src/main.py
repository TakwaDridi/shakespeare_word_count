import re
from collections import Counter
from os.path import join
from pathlib import Path
from string import punctuation

SOURCE_PATH = Path(__file__).parent.parent


def read_file(file_path: str) -> str:
    """
    This function reads the text file and returns it as a string.
    :param file_path: the path to location of text file
    :return:  content of the text file as a python string
    """

    with open(file=file_path, mode='r', encoding="utf8") as f:
        return f.read()


def store_file(text: str, file_path: str):
    """
    :param text:
    :param file_path:
    :return:
    """
    with open(file=file_path, mode='w', encoding='utf8') as f:
        f.write(text)


def clean_text(text: str,
               excluded_punctuation: str) -> str:
    """
    This function performs some elementary operations on the text
    and returns a clean text ready to be counted.

    :param text: the text extracted from the Tempest file
    :param excluded_punctuation : tolerated punctuation characters
    :return: clean text
    """
    _translation_table = str.maketrans('', '', ''.join(excluded_punctuation))
    _punctuation = punctuation.translate(_translation_table)
    regex = re.compile('[%s]' % re.escape(_punctuation))
    return regex.sub(' ', text.lower())


def count_words_in_text(text: str) -> dict:
    """
    This function counts the occurrence of every word in a text,
    words are supposedly separated by a space character.
    :param text: the text extracted from the Tempest file and cleaned
    :return: a dictionary with all words as key and their occurrence as value
    """
    text = " ".join(text.strip().split())
    return Counter(text.split(" "))


def print_top_n_words(word_count: dict,
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


if __name__ == "__main__":
    input_file_path = join(SOURCE_PATH, 'data', 'Tempest.txt')
    text = read_file(file_path=input_file_path)

    text = clean_text(text=text, excluded_punctuation="-'")

    output_file_path = join(SOURCE_PATH, 'data', 'processed_text.txt')
    store_file(text=text, file_path=output_file_path)

    word_count = count_words_in_text(text=text)
    print_top_n_words(word_count=word_count, n=10)
