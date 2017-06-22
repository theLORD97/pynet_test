#!/usr/bin/env python

ip_addr = raw_input("Please enter IP address:")

split = ip_addr.split(".")
print split

split[-1] = 0
print split


