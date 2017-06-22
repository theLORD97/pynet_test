#!/usr/vin/env python

from __future__ import print_function

name1 = "Connor Mcdavid"
name2 = "Leon Draisaitle"
name3 = "Cam Talbot"

try:
    # PY2
    name4 = raw_input("Enter fourth name: ")
except NameError:
    # PY3
    name4 = input("Enter fourth name: ")

print("{:>30}{:>30}{:>30}{:>30}".format("1st Star", "2nd Star", "Goalie", "4th line plug"))
print("{:>30}{:>30}{:>30}{:>30}".format("------", "-------", "-----", "------"))
print("{:>30}{:>30}{:>30}{:>30}".format(name1, name2, name3, name4))
print("\n")



