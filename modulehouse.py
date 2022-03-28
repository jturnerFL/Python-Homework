from math import radians
from pickletools import read_unicodestring1
from re import S
from this import s


def squareFoot(s):
    return s*s
print("Enter the side length of Square: ", end="")
l = float(input())
a = squareFoot(l)
print("\nArea = {:.2f}".format(a))

import math 

def circumFerence():
    return 3.14*r*r

print("Enter Radius of Circle: ", end="")
r = float(input())

c = circumFerence(r)
print("\nCircumference = {:.2f}".format(c))
