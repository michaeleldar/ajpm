#!/usr/bin/python3
from sys import argv
from os import system, mkdir
from random import randint
from os.path import isdir

dir_name = randint(1111111, 9999999)

if not isdir("/etc/ajpm"):
    mkdir("/etc/ajpm")
    installedpkg_file = open("/etc/ajpm/installedpkgs", "w")
    installedpkg_file.write("ajpm")

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
--------------------------------------------------------------------
Licence: GPLv3
--------------------------------------------------------------------
Usage:
ajpm -h or --help | prints help information.
ajpm -v or --version | prints version.
sudo ajpm -uc or updatecatalouge | updates list of avalible packages.
sudo ajpm -um or updatemanager | updates package manager.
testing
        """
        )
    elif argv[1] == "-uc" or argv[1] == "updatecatalogue":
        system(
            "curl https://raw.githubusercontent.com/michaeleldar/ajpm-db/main/packagelist.txt -o /etc/ajpm/pkglist"
        )
    elif argv[1] == "-um" or argv[1] == "updatemanager":
        system(f"mkdir /tmp/{dir_name}")
        system(
            f"curl https://raw.githubusercontent.com/michaeleldar/ajpm/master/filelist -o /tmp/{dir_name}/filelist"
        )
        system(
            f"curl https://raw.githubusercontent.com/michaeleldar/ajpm/master/filenames -o /tmp/{dir_name}/filenames"
        )

        filelist = open(f"/tmp/{dir_name}/filelist", "r")
        filenames = open(f"/tmp/{dir_name}/filenames", "r")

        filesstring = filelist.read()
        filenamesstr = filenames.read()

        filelist.close()
        filenames.close()
        system(f"rm /tmp/{dir_name}/filelist")
        system(f"rm /tmp/{dir_name}/filenames")

        fileslist = filesstring.split("\n")
        filenameslst = filenamesstr.split("\n")
        filenameindex = 0
        for file in fileslist:
            if file == "":
                continue
            filename = filenameslst[filenameindex]
            system(f"curl {file} -o /tmp/{dir_name}/{filename}")
            filenameindex = filenameindex + 1
        print(dir_name)
        system(f"cd /tmp/{dir_name} && make install")
        system(f"rm -r /tmp/{dir_name}")
