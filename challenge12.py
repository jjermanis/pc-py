#!/usr/bin/env python3

from common import authentication_help

# Make sure that image file indicated in the page source exists locally
LOCAL_IMAGE_PATH = "evil2.gfx"


def main():
    try:
        with open(LOCAL_IMAGE_PATH, "r") as _:
            pass
    except FileNotFoundError:
        print("Please download the evil2.gfx from challenge 12, and save it as evil2.gfx")
        print("in this local folder.  ")
        exit()

    # There are five image files interleaved byte-by-byte in the .gfx file.  Write out each image separately.

    # Different image formats, indicated by varying file signatures.
    extensions = ['jpg', 'png', 'gif', 'png', 'jpg']

    data = open("evil2.gfx", "rb").read()
    for i in range(5):
        open(f'{i}.{extensions[i]}', 'wb').write(data[i::5])
    print("As you can see, this does not print the result in a traditional format.")
    print("Use the standard format of: http://www.pythonchallenge.com/pc/return/{answer}.html")
    print("Open image files 0.jpg, 1.png, 2.gif, and 3.png to get the answer.")
    print("4.jpg is not necessary - the image shows crossed out text.")
    print("3.png is damaged.  Try different image viewers.  If that doesn't work... it says 'ional'.")
    authentication_help("return")


if __name__ == "__main__":
    main()
