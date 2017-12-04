#!/usr/bin/env python3

from common import show_def_result, text_from_file


def main():
    # Find the rare characters "in the mess" from the HTML source...  I stored "the mess" in a file.
    raw_data = text_from_file("challenge02text.txt")

    # Get frequency of each character
    histogram = {}
    for c in raw_data:
        histogram[c] = histogram.get(c, 0) + 1

    # Get the "rare" characters.  What does "rare" mean?  In this case, it turns out "rare" means unique.
    # But checking for any relatively small number gets the right answer
    result = ''.join(c for c in raw_data if histogram[c] < 5)
    show_def_result(result)


if __name__ == "__main__":
    main()
