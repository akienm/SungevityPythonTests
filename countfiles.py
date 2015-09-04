#!/usr/bin/python

# Aug 21 2015 Akien MacIain

# 1.	Implement a utility that counts the total number of files in a directory tree.

import os
import sys


def print_usage():
    """ prints out usage information """

    print "countfiles.py\n"
    print "Counts the number of files in a directory tree. Note that all"
    print "directories encountered also count as files.\n"
    print "usage: countfiles.py <dirname>"
    print "     dirname = directory to start from.\n"
    print "Result written to stdout.\n"


def tree_count(dirname):
    """ counts the entities in a given directory tree
    :param dirname: the directory to start from
    :return: number of files (including directories) found in the specified tree
    """
    counter = 0
    for curr_dir, dirs, files in os.walk(dirname):
            counter += len(dirname)
            counter += len(files)

    return counter

arglist = sys.argv
arglist.remove(arglist[0])
if "-h" in arglist or arglist == []:
    print_usage()
    exit(0)

dirname = arglist[0]
print tree_count(dirname)

