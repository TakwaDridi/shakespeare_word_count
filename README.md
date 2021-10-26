# A Shakespeare play word count

This project is written in python. The goal is to count unique words from an English text file, treating hyphen and
apostrophe as part of the word, and to output the n most frequent words and their number of occurrences.

## Environment and Requirements

First, you can create a [conda](https://docs.conda.io/en/latest/) virtual environment or you can work in an existing
environment (for this, you can skip the first two command lines)
All requirements for this project are found in the **`requirements.txt`** file. To install all packages, please use the
following command using the package manager [pip](https://pip.pypa.io/en/stable/)

```bash
$ conda create --name Environment_name python=3.9
$ conda activate Environment_name
$ pip install -r .\requirements.txt
```

## Project organization

```bash
├─data    # the directory containing the text file to be treated   
└─src     # source code and main file
```

## Running

To run the program, you can directly run the main file without precising any arguments. This will launch the program
with the default values of the input text and output file paths. The input text file by default is **`Tempest.txt`** , a
Shakespeare play, is found in the data directory. All output file saves will be found in the data directory as well,
unless given otherwise. first of all open the project directory:

````bash
$ cd project_directory/src
$ python main.py
````

You can also run the main file with the option of choosing the paths of the input and output files and passing them as
arguments:

````bash
$ python main.py --input_file_path <path-to-input-file/file.txt> --output_file_path <path-to-output-file/file.txt>
````

Results will be printed by the program and the processed text will be saved in the output file path that you will have
precised or in the data directory by default.
