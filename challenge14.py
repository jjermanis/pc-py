#!/usr/bin/env python3

# Requires pillow, the Python3 version of PIL
# Be sure to pip3 pillow
from PIL import Image
from common import does_file_exist, authentication_help

LOCAL_IMAGE_PATH = "wire.png"


def main():
    if not does_file_exist(LOCAL_IMAGE_PATH, "Challenge 14"):
        exit()
    img = Image.open(LOCAL_IMAGE_PATH)
    out = Image.new("RGB", (100, 100))
    pixel = 0
    for step in range(100, 50, -1):
        for x in range(100-step, step): #0 to 99
            out.putpixel((x, 100-step), img.getpixel((pixel, 0)))
            pixel += 1
        for y in range(100-step+1, step): # 1 to 99
            out.putpixel((step-1, y), img.getpixel((pixel, 0)))
            pixel += 1
        for x in range(step-2, 100-step-1, -1): #98 to 0
            out.putpixel((x, step-1), img.getpixel((pixel, 0)))
            pixel += 1
        for y in range(step-2, 100-step, -1): # 98 to 1
            out.putpixel((100-step, y), img.getpixel((pixel, 0)))
            pixel += 1
    out.show()
    print("As you can see, this does not print the result in a traditional format.")
    print("Use the standard format of: http://www.pythonchallenge.com/pc/return/{answer}.html")
    print("(when you get to that page, switch the URL to the name that's provided)")
    authentication_help()


if __name__ == "__main__":
    main()
