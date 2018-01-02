#!/usr/bin/env python3

from urllib.request import urlopen, Request
from urllib.error import HTTPError
from base64 import b64encode
from re import search

IMG_URL = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
CREDENTIALS = b"butter:fly"
B64_CREDENTIALS = b64encode(CREDENTIALS)
BASIC_AUTH = B64_CREDENTIALS.decode()
RESULT_FILE = "challenge_21.zip"


def open_from_range(range_start):
    request = Request(IMG_URL)
    request.add_header("Authorization", f"Basic {BASIC_AUTH}")
    request.add_header("Range", f"bytes={range_start}-")
    response = urlopen(request)
    content_range = response.headers['Content-Range']
    range_start, range_end, length = search("bytes (\d+)-(\d+)/(\d+)", content_range).groups()
    return response, range_start, range_end, length


def main():
    # The "trick" with this one is that the server is "communicating" through the "Content-Range" header.
    # To start, the header indicates a truncated response.  Request the data + 1 byte
    range_start = "0"
    length = -1
    while True:
        try:
            response, _, range_end, length = open_from_range(range_start)
            # Don't print the first response - it's the JPEG from the challenge page.
            if range_start != "0":
                print(response.read().decode().strip())
            # Ask for the content after the most recent range
            range_start = int(range_end) + 1
        except HTTPError:
            # Server (intentionally) returns a 416 at the end of the range.
            break
    # Now we "are in."  Let's get out and request beyond the end of the range
    response, range_start, _, _ = open_from_range(length)
    print(response.read().decode().strip())

    # That was backwards.  Reverse our previous iteration strategy
    range_start = int(range_start) - 1
    response, _, _, _ = open_from_range(range_start)

    # The challenge 21 file "is hiding" at a certain offset.  Get it and save it.
    hiding_text = response.read().decode()
    print(hiding_text)
    hidden = search("and it is hiding at (.+)\.", hiding_text).group(1)
    response, _, _, _ = open_from_range(hidden)
    result = open(RESULT_FILE, "wb")
    result.write(response.read())

    print('This is DEFINITELY not a traditional problem.  In fact, challenge #21 has been')
    print(f'downloaded as {RESULT_FILE}.  The file is password protected.  As indicated')
    print('in the "dialog", the password is what you get called, in reverse ("redavni").')


if __name__ == "__main__":
    main()
