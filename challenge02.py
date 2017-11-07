# Find the rare characters "in the mess" from the HTML source...  I stored "the mess" in a file.
text_file = open("challenge02text.txt", "r")
raw_data = ""
for line in text_file.readlines():
    raw_data += line
text_file.close()

# Get frequency of each character
histogram = {}
for c in raw_data:
    histogram[c] = histogram.get(c, 0) + 1

# Get the "rare" characters.  What does "rare" mean?  In this case, it turns out "rare" means unique.
# But checking for any relatively small number gets the right answer
result = ''.join(c for c in raw_data if histogram[c] < 5)
print(f"http://www.pythonchallenge.com/pc/def/{result}.html")
