#!/usr/bin/env python3

from string import ascii_lowercase
from common import show_def_result

# The hint on the page.  The images indicates that each character should be rotated forward two spots.
# When decrypted, this hint suggests using maketrans()... which is deprecated in Python3.
HINT = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq
glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. 
lmu ynnjw ml rfc spj."""

# The hint, when decrypted, indicates to decrypt the URL... well, not the _whole_ URL
URL_FRAGMENT = "map"

# Map lower case characters to the characters two spot forward
left = ascii_lowercase
right = ascii_lowercase[2:]+ascii_lowercase[:2]


# Translate the character if it's lower case.  Otherwise (e.g. punctuation, spaces) leave it alone.
def translate(c):
    return right[left.find(c)] if left.find(c) > -1 else c


# Translate each character in the input string
def decrypt(x):
    return ''.join(translate(c) for c in x)


def main():
    print(f"Message: {decrypt(HINT)}")
    print()
    answer = decrypt(URL_FRAGMENT)
    show_def_result(answer)


if __name__ == "__main__":
    main()
