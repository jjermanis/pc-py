from string import ascii_lowercase

# The hint on the page.  The images indicates that each character should be rotated forward two spots.
# When decrypted, this hint suggests using maketrans()... which is deprecated in Python3.
hint = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq
glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. 
lmu ynnjw ml rfc spj."""

# The hint, when decrypted, indicates to decrypt the URL... well, not the _whole_ URL
url_fragment = "map"

# Map lower case characters to the characters two spot forward
left = ascii_lowercase
right = ascii_lowercase[2:]+ascii_lowercase[:2]


# Translate the character if it's lower case.  Otherwise (e.g. punctuation, spaces) leave it alone.
def translate(c):
    return right[left.find(c)] if left.find(c) > -1 else c


# Translate each character in the input string
def decrypt(x):
    return ''.join(translate(c) for c in x)


print(f"Message: {decrypt(hint)}")
print()
answer = decrypt(url_fragment)
print(f"http://www.pythonchallenge.com/pc/def/{answer}.html")
