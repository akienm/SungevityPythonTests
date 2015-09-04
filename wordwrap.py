#!/usr/bin/python

# Aug 21 2015 Akien MacIain

# 3.	Implement a "word wrap" utility that takes a string of any length and breaks it
# up into a list of newline-delimited strings.  Each string consists of a number of space
# or period delimited words.  Each string must be the maximum length <= 80 characters that
# does not break a word up.

import sys
import textwrap

def print_usage():
    """ prints out usage information """

    print "wordwrap.py\n"
    print "takes in input file name, and word wraps that file to stdout\n"
    print "usage: wordwrap.py myfile\n"


arglist = sys.argv
arglist.remove(arglist[0])
if "-h" in arglist or arglist == []:
    print_usage()
    exit(0)

file_handle = open(arglist[0], 'r')
file_data = file_handle.read()
wrapped_data = textwrap.wrap(file_data, 80)
for item in wrapped_data:
    print item

