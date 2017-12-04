#!/usr/bin/env python3

from common import show_def_result
import urllib.request


def main():
    print("This one takes a long time - many URLs need to be retrieved")

    # Follow the chain of URLs indicated.  The responses are human-readable, and logic is driven to parse it out.

    nothing = '12345'  # this the first "nothing" value provided in the original page
    data = ""
    for _ in range(400):  # the page says that no more than 400 tries should be needed
        url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}"
        data = urllib.request.urlopen(url).read().decode("utf-8")
        nothing_index = data.find("and the next nothing is ")
        if nothing_index >= 0:
            nothing = data[nothing_index + 24:]
        elif data.find("Divide by two") >= 0:  # this appears once in the chain
            nothing = int(nothing) // 2
        elif data.find('.html'):  # a resource name is the answer
            break
    result = data[:data.find('.html')]
    show_def_result(result)


if __name__ == "__main__":
    main()
