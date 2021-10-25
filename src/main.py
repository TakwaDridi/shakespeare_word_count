import argparse

import file_handler as fh
import preprocess
import visualize

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('--input_file_path',
                            required=False,
                            default=fh.get_default_file_path('Tempest.txt'),
                            help='Local path to the input text file')

    arg_parser.add_argument('--output_file_path',
                            required=False,
                            default=fh.get_default_file_path('result.txt'),
                            help='Local path to the output text file')

    args = arg_parser.parse_args()

    # ================ process text ============
    text = fh.read_file(file_path=args.input_file_path)
    text = preprocess.clean_text(text=text, excluded_punctuation="-'")
    fh.store_file(text=text, file_path=args.output_file_path)

    # =========== print results ==============
    text = fh.read_file(args.output_file_path)
    word_count = preprocess.count_words_in_text(text=text)
    visualize.show_top_n_words(word_count=word_count, n=10)
