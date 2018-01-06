#!/usr/bin/env python3

from common import does_file_exist, authentication_help
import zlib
import bz2

LOCAL_FILE_PATH = "challenge_21/package.pack"

ZLIB_SIG = b"x\x9c"
BZIP2_SIG = b"BZh"


def main():
    if not does_file_exist(LOCAL_FILE_PATH, "Challenge 21"):
        exit()
    with open(LOCAL_FILE_PATH, "rb") as pack_file:
        data = pack_file.read()
    logs = ""
    while True:
        if data[0:2] == ZLIB_SIG:
            # zlib file signature
            data = zlib.decompress(data)
            logs += '.'
        elif data[0:3] == BZIP2_SIG:
            # Bzip2 file signature
            data = bz2.decompress(data)
            logs += 'X'
        elif data[-2:] == ZLIB_SIG[::-1]:
            # Hint in readme ("I looked backwards") indicates that the data may need to be reversed
            # zlib file signature is at end - reverse
            data = data[::-1]
            logs += '\n'
        elif data[-3:] == BZIP2_SIG[::-1]:
            # Bzip2 file signature is at end - reverse
            data = data[::-1]
            logs += '\n'
        else:
            break
    print(data)
    print(logs)
    print("As you can see, this does not print the result in a traditional format.")
    print("Use the standard format of: http://www.pythonchallenge.com/pc/hex/{answer}.html")
    authentication_help("hex")


if __name__ == "__main__":
    main()
