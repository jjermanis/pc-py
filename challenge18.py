#!/usr/bin/env python3

from common import does_file_exist
from difflib import Differ
import gzip

LOCAL_FILE_PATH = "deltas.gz"


def get_image_files():

    if not does_file_exist(LOCAL_FILE_PATH, "Challenge 18"):
        exit()

    def out_file(desc):
        return open(f"c18_{desc}.png", "wb")

    with gzip.open(LOCAL_FILE_PATH) as content:
        left, right = [], []
        for line in content:
            left.append(line[:54].decode().strip() + "\n")
            right.append(line[54:].decode().strip() + "\n")
        compare = Differ().compare(left, right)

    with out_file("username") as left_file, out_file("password") as right_file, out_file("url") as both_file:
        for line in compare:
            bs = bytes.fromhex(line[2:].strip())
            if line[0] == '+':
                left_file.write(bs)
            elif line[0] == '-':
                right_file.write(bs)
            elif line[0] == ' ':
                both_file.write(bs)
            else:
                raise Exception(f"Unhandled diff type: {line[0]}")


def main():
    get_image_files()
    print("As you can see, this does not print the result in a traditional format.")
    print("This solution created three files, all starting with c18_")
    print("The url file tells you the (relative) URL for the answer.")
    print("This new folder requires basic auth.  The user and password files show the credentials.")
    print("Use the standard format of: http://www.pythonchallenge.com/pc/hex/{answer}.html")


if __name__ == "__main__":
    main()
