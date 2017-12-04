#!/usr/bin/env python3

from common import show_return_result


def main():
    # Continue the pattern.  Each term is a description of the previous.
    # 21 => 1211, because 21 is one 2 and one 1.
    curr_term = "1"
    next_term = ""
    for _ in range(30):
        char_index = 0
        ahead_index = 0
        while char_index < len(curr_term):
            while ahead_index < len(curr_term) and curr_term[ahead_index] == curr_term[char_index]:
                ahead_index += 1
            next_term += str(ahead_index - char_index) + curr_term[char_index]
            char_index = ahead_index
        curr_term = next_term
        next_term = ''
    show_return_result(len(curr_term))


if __name__ == "__main__":
    main()
