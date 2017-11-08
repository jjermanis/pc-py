

def show_result(answer):
    print(f"Answer - http://www.pythonchallenge.com/pc/def/{answer}.html")
    print(f"(to go to the solution page, visit http://www.pythonchallenge.com/pcc/def/{answer}.html)")


def text_from_file(filename):
    text_file = open(filename, "r")
    result = ""
    for line in text_file.readlines():
        result += line
    text_file.close()
    return result
