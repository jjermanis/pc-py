#!/usr/bin/env python3

# Requires pillow, the Python3 version of PIL
# Be sure to pip3 pillow
from PIL import Image
from common import authentication_help

# Make sure that image file indicated in the page source exists locally
LOCAL_IMAGE_PATH = "cave.jpg"
IMAGE_URL = "http://www.pythonchallenge.com/pc/return/cave.jpg"


def main():
    try:
        with open(LOCAL_IMAGE_PATH, "r") as _:
            pass
    except FileNotFoundError:
        print("Please download the image from challenge 11, and save it as cave.jpg")
        print("in this local folder.  ")
        exit()

    # The image actually has two distinct pictures within it, alternating pixels.
    # The even pixels are the lower contrast "hidden" picture.
    img = Image.open(LOCAL_IMAGE_PATH)
    width, height = img.size
    even = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            if (x+y) % 2 == 0:
                # Increase brightness to make image readable
                even.putpixel((x, y), (3*pixel[0], 3*pixel[1], 3*pixel[2]))
    even.show()
    print("As you can see, this does not print the result in a traditional format.")
    print("Use the standard format of: http://www.pythonchallenge.com/pc/return/{answer}.html")
    authentication_help()


if __name__ == "__main__":
    main()
