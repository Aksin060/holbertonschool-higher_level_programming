#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        c = str[i]
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print()
