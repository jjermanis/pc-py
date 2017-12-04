#!/usr/bin/env python3

from common import download_file_if_necessary, show_def_result
# Requires pillow, the Python3 version of PIL
# Be sure to pip3 pillow
from PIL import Image

# Make sure that image file indicated in the page source exists locally
LOCAL_IMAGE_PATH = "oxygen.png"
IMAGE_URL = "http://www.pythonchallenge.com/pc/def/oxygen.png"


def main():
    download_file_if_necessary(IMAGE_URL, LOCAL_IMAGE_PATH)

    # The grey colors correspond to ASCII values.  They are in blocks 7 pixels wide
    img = Image.open(LOCAL_IMAGE_PATH)
    msg = ""
    for x in range(0, img.width, 7):
        pixel = img.getpixel((x, img.height/2))
        msg += chr(pixel[0])
    # The message reads: smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]pe_
    # Extract the list from the message, and translate the ASCII from that.
    next_level = msg[msg.find('[')+1:msg.find(']')].split(",")
    answer = ""
    for x in next_level:
        answer += chr(int(x))
    show_def_result(answer)


if __name__ == "__main__":
    main()
