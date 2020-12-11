import argparse
import os
import re
import subprocess

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

def tempCreate(str)->None:
    with open("temp.py", "w") as t:
        t.write(str)


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
            if isCode:
                isCode = False
                fulltext.append(phrase) 
                phrase = ""
            else:
                isCode = True
                fulltext.append(phrase[:-3])
                phrase = "```"
        phrase += text[i]
        i += 1
    fulltext.append(phrase)
    print(fulltext)

    # for val in fulltext:
    #     if val[0] == "`":
    #         tempCreate(val[val.index("\n"):-3])
    #         print(subprocess.check_output(['python3', 'temp.py']))
    #         break
            


def main():
    files = validate_paths(get_args())

    process(files[0], interpreter, shortcode)
    # complete_list = [process(name, interpreter, shortcode) for name in files]

    # for l in complete_list:
    #     for z in l:
    #         print(z)


main()
