#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    allf = dir()
    for n in range(0, len(allf)):
        if allf[n][:2] != "__":
            print("{:s}".format(allf[n]))
