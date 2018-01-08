#!/usr/bin/env python3

# Requires pillow, the Python3 version of PIL
# Be sure to pip3 pillow
from PIL import Image
from common import does_file_exist, authentication_help

LOCAL_FILE_PATH = "white.gif"


def joystick_position(img):
    for y in range(img.height):
        for x in range(img.width):
            if img.getpixel((x, y)) != 0:
                return x, y


def main():
    if not does_file_exist(LOCAL_FILE_PATH, "Challenge 22"):
        exit()
    ox, oy = 40, 50
    with Image.open(LOCAL_FILE_PATH) as gif, Image.new("RGB", (300, 100)) as out:
        for frame_num in range(gif.n_frames):
            gif.seek(frame_num)
            x, y = joystick_position(gif)
            dx, dy = x-100, y-100
            if dx == 0 == dy:
                ox += 40
                oy = 50
            else:
                ox, oy = ox + dx, oy + dy
            out.putpixel((ox, oy), (255, 255, 255))
        out.show()
    print("As you can see, this does not print the result in a traditional format.")
    print("Use the standard format of: http://www.pythonchallenge.com/pc/hex/{answer}.html")
    authentication_help("hex")


if __name__ == "__main__":
    main()
