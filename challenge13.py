#!/usr/bin/env python3

from xmlrpc.client import ServerProxy
from common import show_return_result

# Server linked in the challenge.  The response format on the error indicates XML-RPC.
XMLRPC_URL = "http://www.pythonchallenge.com/pc/phonebook.php"


def server_info():
    # None of this was needed for the final solution.  This is the code to discover what was implemented
    # on the XM-RPC server.
    server = ServerProxy(XMLRPC_URL)
    methods = server.system.listMethods()
    print(methods)
    sig = server.system.methodSignature('phone')
    print(sig)


def main():
    server = ServerProxy(XMLRPC_URL)
    response = server.phone('Bert')
    answer = response[4:].lower()
    show_return_result(answer)


if __name__ == "__main__":
    main()
