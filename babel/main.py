import argparse
import os
import re

# Configuration

interpreter: str = "python3"
shortcode: str = "python"


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_names", nargs="+", help="Markdown files")
    args = parser.parse_args()

    return args


def validate_paths(args) -> list:
    for file_name in args.file_names:
        if not os.path.isfile(file_name):
            if os.path.isdir(file_name):
                raise FileNotFoundError(f"{file_name} is a directory.")
            else:
                raise FileNotFoundError(f"{file_name} is not a file.")

    return args.file_names


def process(name: str, interpreter: str, shortcode: str):
    file = open(name)
    text = file.read()
    file.close()

    fulltext = []
    isCode = False
    phrase = ""
    acceptableCodeRanges = ["`", "~"]
    for i in range(len(text)):
        if text[i-1] in acceptableCodeRanges and text[i-2] in acceptableCodeRanges and text[i-3] in acceptableCodeRanges:
            if code:
                code = False
                fulltext.append(phrase) 
                phrase = ""
            else:
                code = True
                fulltext.append(phrase[:-3])
                phrase = "```"
        phrase += text[i]
        i += 1
    fulltext.append(phrase)
    print(fulltext)


def main():
    files = validate_paths(get_args())

    process(files[0], interpreter, shortcode)
    # complete_list = [process(name, interpreter, shortcode) for name in files]

    # for l in complete_list:
    #     for z in l:
    #         print(z)


main()
