import os
import time

# COLORS
G = '\033[1;34m[*] \033[0m'
S = '\033[1;32m[+] \033[0m'
W = '\033[1;33m[!] \033[0m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'


print(FAIL + """\n
----------------------------------------
|                                      |
|         SPF CHECKER!                 |
|                                      |
----------------------------------------
""" + ENDC)

# CODE STARTS

targ = input(OKGREEN + "\nTarget Domain: " + ENDC)

os.system("dig TXT " + targ + "| grep IN > spf.txt ")
time.sleep(2)

with open('spf.txt') as f:
    if '~all' in f.read():
        print("\n" + G + "It can be injectable goo exploit!" + ENDC)
