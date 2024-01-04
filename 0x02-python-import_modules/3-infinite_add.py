#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sumint = 0
    for n in range(1, len(argv)):
        sumint += int(argv[n])
    print("{}".format(sumint))
