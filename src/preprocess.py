import re
from collections import Counter
from string import punctuation


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
