#!/usr/bin/env python3

import this
import codecs
from re import search
from common import show_hex_result


def hint():
    print(codecs.encode("va gur snpr bs jung?", "rot_13"))


def main():
    hint()
    zen = codecs.encode(this.s, "rot_13")
    answer = search("the face of ([a-z]+)", zen).group(1)
    print()
    show_hex_result(answer)


if __name__ == "__main__":
    main()
