import argparse
import os
import re

# Configuration

extension: str = "py"


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


def main():
    files = validate_paths(get_args())

    for name in files:
        f = open(name)
        text = f.read()
        f.close()
        



if __name__ == "__main__":
    main()