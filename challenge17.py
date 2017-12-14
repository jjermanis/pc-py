#!/usr/bin/env python3

from urllib.request import urlopen, Request
from re import search
import bz2
from urllib.parse import unquote_to_bytes
from challenge13 import phone


def research():
    # This isn't necessary for the final solution.  This was code that was used to figure out the approach
    # The inset picture is the same from challenge 4.  Use the same URL
    url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php"
    request = urlopen(url)
    data = request.read()
    print(data)
    headers = request.getheaders()
    # The cookie provides the approach for this problem
    print(headers)


def get_header_cookie(headers):
    for key, value in headers:
        if key == 'Set-Cookie':
            return value
    raise Exception("No Set-Cookie key found")


def get_message():
    # Start with 12345, like in problem 4
    busynothing = "12345"
    cookie_msg = ""
    for _ in range(400):
        url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={busynothing}"
        request = urlopen(url)

        # Read the next byte in the cookie
        headers = request.getheaders()
        cookie = get_header_cookie(headers)
        cookie_msg += search("info=([^;]+);", cookie).group(1)

        # The next busynothing is in the response
        data = request.read().decode("utf-8")
        re = search("the next busynothing is (\d+)", data)
        if re is None:
            break
        busynothing = re.group(1)

    # Convert to bytes and decompress.  The spaces were URL encoded though
    res = unquote_to_bytes(cookie_msg.replace("+", " "))
    decoded = bz2.decompress(res).decode()
    print(f"Decoded from cookies: {decoded}")
    return search('"(.+)"', decoded).group(1)


def send_message(url, message):
    req = Request(url, headers={"Cookie": "info=" + message.replace(" ", "+")})
    return urlopen(req).read().decode("utf-8")


def main():
    message = get_message()
    print("26th refers to Mozart.  His father is Leopold.  We'll phone him.")
    phone_number = phone("Leopold")
    print(f"Phone response: {phone_number}")
    leopold_url = f"http://www.pythonchallenge.com/pc/stuff/{phone_number[4:].lower()}.php"
    print(f"Send our message ({message}) to {leopold_url}")
    response = send_message(leopold_url, message)
    print("Here is the HTML we get back - note the text at the bottom.")
    print(response)
    print("As you can see, this does not print the result in a traditional format.")
    print("Use the standard format of: http://www.pythonchallenge.com/pc/stuff/{answer}.html")


if __name__ == "__main__":
    main()
