#!/usr/bin/env python3

import datetime
from common import show_return_result


def find_second_youngest():
    is_found_youngest = False
    for year in range(1996, 1016, -20):
        if datetime.date(year, 1, 26).isoweekday() == 1:
            if not is_found_youngest:
                is_found_youngest = True
            else:
                return year


def main():
    year = find_second_youngest()
    print(f"The year is {year}.  The date (hinted in the page source) is January 27, {year}.")
    print("This does not provide an answer in a traditional format.  You need to know what happened on that date.")
    print("Mozart was born.  This is the answer to this problem")
    show_return_result("mozart")


if __name__ == "__main__":
    main()
