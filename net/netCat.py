#! /usr/bin/env python2

import sys
import socket
import getopt
import threading
import subprocess

listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

def usage():
    print "netcat tool"
    print
    print "netCat.py -t target_host -p port"
    print "-l --listen"
    print "-e --execute=file_to_run"
    print "-c --commandshell"
    print "-u --upload=destination"
    print
    print "example:"
    print "netCat.py -t 192.168.0.1 -p 5555 -l -c"
    print "netCat.py -t 192.168.0.1 -p 5555 -l -u=./file.o"
    print "netCat.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\""
    print "echo ''ABC' | netCat.py -t 192.16811.12 -p 135"
    sys.exit(0)

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:", ["help", "listen", "target", "port", "command", "upload"])
    except getopt.GetoptError as err:
        print str(err)
        usage()

    for o,a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-e", "--excute"):
            execute = a
        elif o in ("-c", "--commandshell"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port = int(a)
        else:
            assert False, "no this option"

main()
