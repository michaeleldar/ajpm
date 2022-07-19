#!/usr/bin/python3
from sys import argv
from os import system, mkdir
from random import randint
from os.path import isdir

dir_name = randint(1111111, 9999999)

if not isdir("/etc/jdpkg"):
    mkdir("/etc/jdpkg")

if argv.__len__() == 1:
    print("Run ajpm -h or ajm --help for help.")
    quit()
elif argv.__len__() == 2:

    if argv[1] == "-v" or argv[1] == "--version":
        print("1.0.0-dev")

    elif argv[1] == "-h" or argv[1] == "--help":
        print(
            """
Ajpm
--------------------------------------------
Licence: GPLv3
--------------------------------------------
Usage:
ajpm -h or --help | prints help information.
ajpm -v or --version | prints version.
        """
        )
    elif argv[1] == "-uc" or argv == "updatecat":
        system(f"mkdir /tmp/{dir_name}")
        system("")
        system(f"rm -rv /tmp/{dir_name}")
        system(
            f"curl https://raw.githubusercontent.com/michaeleldar/ajpm-db/main/packagelist.txt -o /etc/jdpkg"
        )
