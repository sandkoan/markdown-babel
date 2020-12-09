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

    with open(name) as f:
        hunks: list = []
        mini_lines: list = []
        is_code: bool = False

        for i in f.readlines():
            if (i == f"```{shortcode}") or (i == f"~~~{shortcode}"):
                is_code = True
            if is_code and (i != "```" or i != "~~~"):
                mini_lines.append(i)
            else:
                hunks.append(mini_lines)
                mini_lines.clear()
                is_code = False

        print(hunks)


def main():
    files = validate_paths(get_args())

    process(files[0], interpreter, shortcode)
    # complete_list = [process(name, interpreter, shortcode) for name in files]

    # for l in complete_list:
    #     for z in l:
    #         print(z)


main()
