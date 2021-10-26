from os.path import join
from pathlib import Path

SOURCE_PATH = Path(__file__).parent.parent


def get_default_file_path(file_name: str) -> str:
    """
    This function takes as input a file name and returns
    the absolute path to this file in the data directory.
    :param file_name: a string containing the name of thee text file
    :return: a string containing the absolute path to the text file
    from the data directory
    """
    return join(SOURCE_PATH, 'data', file_name)


def read_file(file_path: str) -> str:
    """
    This function reads the text file and returns it as a string.

    :param file_path: the path to location of text file
    :return:  content of the text file as a python string
    """
    try:
        with open(file=file_path, mode='r', encoding="utf8") as f:
            return f.read()

    except FileNotFoundError:
        raise FileNotFoundError(f'No text file was found at location {file_path}')


def store_file(text: str, file_path: str) -> None:
    """
    This function creates a file and writes a text into it.

    :param text: a string containing the desired text to be stored
    :param file_path: a string containing the absolute path to where one
    wishes to store the text file
    """
    with open(file=file_path, mode='w', encoding='utf8') as f:
        f.write(text)
