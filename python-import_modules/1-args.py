#!/usr/bin/python3
#import system module
import sys
#script ran directly or being imported as module
if __name__ == "__main__":
#number of arguments declared
    argum = len(sys.argv) - 1
#if no argument and print
    if argum == 0:
        print("0 arguments.")
#elif 1 argument and print
    elif argum == 1:
        print("1 argument.")
#else there are more than 1 arguments and print
    else:
        print("{:d} arguments:".format(argum))
#loop the arguments
    for i in range(1, argum + 1):
#print arguments using string format
        print("{:d}: {:s}".format(i, sys.argv[i]))
