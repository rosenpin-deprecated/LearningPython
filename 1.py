#!/usr/bin/python
import sys
import os
import string
import math

print os.environ
os.system("ls -al")
a = "hello"
print a.replace("h", "b")
print string.punctuation
print math.factorial.__doc__


# Pass by reference test
def change_list_value(l):
    l[1] = "hey, I've been modified!"


myList = ["easy as", "one", "two"]
print myList
change_list_value(myList)
print myList
