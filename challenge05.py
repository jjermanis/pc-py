import urllib.request
import pickle

# This resource is identified in the page source
url = "http://www.pythonchallenge.com/pc/def/banner.p"
data = pickle.loads(urllib.request.urlopen(url).read())

for row in data:
    line = ""
    for char, count in row:
         line += count * char
    print(line)

print("As you can see, this does not print the result in a traditional format.")
print("Use the standard format of: http://www.pythonchallenge.com/pc/def/{answer}.html")
