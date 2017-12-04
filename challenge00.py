#!/usr/bin/env python3

from common import show_def_result


def main():
    # Yes, 2**38 also works here, but I was playing with using ranges here
    result = 1
    for _ in range(38):
        result *= 2
    show_def_result(result)


if __name__ == "__main__":
    main()
