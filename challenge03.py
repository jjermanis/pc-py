#!/usr/bin/env python3

from common import show_def_result, text_from_file
import re


def main():
    s = text_from_file("challenge03text.txt")

    # "One small letter, surrounded by EXACTLY three big bodyguards on each of its sides."
    # Look for a lower case letter, with three upper case letters on either side, PLUS a lower case
    # letter on either side of THAT (to enforce "EXACTLY three" upper case letter).
    result = "".join(re.findall("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", s))
    show_def_result(result)
    print("Note: that page is supposed to redirect... but for me it did not.  Change the URL to match")
    print("what is shown in the browser.")


if __name__ == "__main__":
    main()
