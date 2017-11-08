from common import show_result, text_from_file
import re

s = text_from_file("challenge03text.txt")

# "One small letter, surrounded by EXACTLY three big bodyguards on each of its sides."
# Look for a lower case letter, with three upper case letters on either side, PLUS a lower case
# letter on either side (to enforce "EXACTLY three" upper case letter).
result = "".join(re.findall("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", s))
show_result(result)
