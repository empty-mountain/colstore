"""test something here。
"""
import time
import string
import random

dicts = {
    0: list(string.ascii_letters),
    1: list(string.printable[:-6]),
}


print(dicts[1])