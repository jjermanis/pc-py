import urllib.request
import challenge08


def show_def_result(answer):
    print(f"Answer - http://www.pythonchallenge.com/pc/def/{answer}.html")
    print(f"(to go to the solution page, visit http://www.pythonchallenge.com/pcc/def/{answer}.html)")


def show_return_result(answer):
    print(f"Answer - http://www.pythonchallenge.com/pc/return/{answer}.html")
    print(f"(to go to the solution page, visit http://www.pythonchallenge.com/pcc/return/{answer}.html)")
    authentication_help("return")


def show_hex_result(answer):
    print(f"Answer - http://www.pythonchallenge.com/pc/hex/{answer}.html")
    print(f"(to go to the solution page, visit http://www.pythonchallenge.com/pcc/hex/{answer}.html)")
    authentication_help("hex")


def text_from_file(filename):
    text_file = open(filename, "r")
    result = ""
    for line in text_file.readlines():
        result += line
    text_file.close()
    return result


def download_file_if_necessary(url, local_path):
    try:
        with open(local_path, "r") as _:
            pass
    except:
        urllib.request.urlretrieve(url, local_path)


def does_file_exist(filename, challenge_name):
    try:
        with open(filename, "r") as _:
            return True
    except FileNotFoundError:
        print(f"Please download {filename} from {challenge_name} and save to this local folder.")
        return False


def authentication_help(folder):
    print("You may be prompted for simple auth credentials.  Here they are if you need them.")
    if folder == "return":
        username, password = challenge08.get_credentials()
        print(f"Username: {username}")
        print(f"Password: {password}")
    elif folder == "hex":
        print("For this username and password, run challenge18 and look at the c18_ files.")
    else:
        raise Exception(f"Unknown folder: {folder}")
