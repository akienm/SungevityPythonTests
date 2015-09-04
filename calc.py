#!/usr/bin/python

# Aug 21 2015 Akien MacIain

# 2.	Implement a simple calculator that can perform the following operations: *, /, +, -
# on integers or floats. This calculator may display the result of a calculation any way you choose.

import sys
import operator


def print_usage():
    """ prints out usage information """

    print "calc.py\n"
    print "performs simple math from the command line"
    print "+ - * and / are supported.\n"
    print "usage: calc.py n1 [+, -, *, /] n2\n"
    print "Result written to stdout.\n"


arglist = sys.argv
arglist.remove(arglist[0])
if "-h" in arglist or arglist == []:
    print_usage()
    exit(0)

funcdict = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.div
}

typedict = {
    True: float,
    False: int
}


n1 = arglist[0]
n1 = typedict['.' in n1](n1)
n2 = arglist[2]
n2 = typedict['.' in n2](n2)
op = funcdict[arglist[1]]
print op(n1, n2)
