#!/usr/bin/env python3

from sys import argv

def main():

    # argv is an array, the first value is the name of the 
    # program called
    print("Name of program called :: ", argv[0])

    # check the length to see if an argument was supplied
    if len(argv) < 2:
        print("No arguments supplied")
        return

    # print the first argument supplied
    print("Argurment supplied :: ", argv[1])
    return

if __name__ == '__main__':
    main()
