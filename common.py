import urllib.request
from challenge08 import get_credentials

def show_def_result(answer):
    print(f"Answer - http://www.pythonchallenge.com/pc/def/{answer}.html")
    print(f"(to go to the solution page, visit http://www.pythonchallenge.com/pcc/def/{answer}.html)")


def show_return_result(answer):
    print(f"Answer - http://www.pythonchallenge.com/pc/return/{answer}.html")
    print(f"(to go to the solution page, visit http://www.pythonchallenge.com/pcc/return/{answer}.html)")
    authentication_help()


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


def authentication_help():
    print("You may be prompted for simple auth credentials.  Here they are if you need them.")
    username, password = get_credentials()
    print(f"Username: {username}")
    print(f"Password: {password}")
