#!/usr/bin/env python3

# Requires pillow, the Python3 version of PIL
# Be sure to pip3 pillow
from PIL import Image
from common import does_file_exist, authentication_help

LOCAL_IMAGE_PATH = "mozart.gif"
MAGENTA = (255, 0, 255)


def main():
    if not does_file_exist(LOCAL_IMAGE_PATH, "Challenge 16"):
        exit()
    gif_img = Image.open(LOCAL_IMAGE_PATH)

    # GIF uses a palette.  Convert to RGB values for each pixel
    img = gif_img.convert("RGB")
    out = Image.new("RGB", (img.width, img.height))

    # "Rotate" each row, moving the magenta band to the far left
    for y in range(0, img.height):
        magenta_index = -1
        # Find magenta band
        for x in range(0, img.width):
            if MAGENTA == img.getpixel((x, y)):
                magenta_index = x
                break
        if magenta_index == -1:
            raise Exception(f"Could not find magenta in row #{y}")

        # Rotate the row so that the magenta band is on the far left
        for x in range(0, img.width):
            out.putpixel(((x-magenta_index) % img.width, y), img.getpixel((x, y)))
    out.show()
    print("As you can see, this does not print the result in a traditional format.")
    print("Use the standard format of: http://www.pythonchallenge.com/pc/return/{answer}.html")
    authentication_help()


if __name__ == "__main__":
    main()
