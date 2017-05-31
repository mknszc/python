#!bin/bash/python

def removeLastChar(s):
    if len(s) > 0:
        print(s)
        s = s[:-1]
        removeLastChar(s)
    else:
        pass
