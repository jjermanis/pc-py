#!/usr/bin/env python3

import zipfile
from common import download_file_if_necessary

LOCAL_ZIP_PATH = "channel.zip"
ZIP_URL = "http://www.pythonchallenge.com/pc/def/channel.zip"


def main():
    # Make sure that ZIP file indicated in the page source exists locally
    download_file_if_necessary(ZIP_URL, LOCAL_ZIP_PATH)

    with zipfile.ZipFile(LOCAL_ZIP_PATH) as channel_zip:
        # readme in the zip says to start at 90052
        curr = "90052"
        comments = ""

        data = ""
        while data != "Collect the comments.":
            file_name = f"{curr}.txt"
            data = channel_zip.read(file_name).decode("utf-8")
            comments += channel_zip.getinfo(file_name).comment.decode("utf-8")
            curr = data[16:]
    print(comments)

    print("As you can see, this does not print the result in a traditional format.")
    print("Use the standard format of: http://www.pythonchallenge.com/pc/def/{answer}.html")
    print('If you use the large block letters, you will be told "it\'s in the air. look at the letters."')
    print("Use the letters that make up the block letters.")


if __name__ == "__main__":
    main()
