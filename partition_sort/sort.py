'''
This Python code was written in code challenge to partition sort a strings in text file
and insert the output in another file.

By: Ahmad Habaybeh
08/06/2022

'''

# import needed libraries
from random import randint
import numpy as np
import getopt
import sys
filename = "input.txt"
output = "my-output1.txt"

# function that will sort input arrays using quick sort and resturn a sorted array either numeric or alphabet
def quick_sort(l):
    if len(l) < 2:
        return l
    low, same, high = [], [], []
# choose a randon pivot
    pivot = l[randint(0, len(l)-1)]
    for i in l:
        if i < pivot:
            low.append(i)
        elif i == pivot:
            same.append(i)
        elif i > pivot:
            high.append(i)

    return quick_sort(low) + same + quick_sort(high)

# a function that will split the provided array into smaller arrays of similar datatype either numberic or alphabet
def create_partition (lst):
    nm = []
    cr = []
    ttl = []
    cnt = 0
    for i in lst:
        if (i.isnumeric()):
            # check if the character list is not empty and add it to final array.
            if (len(cr) > 0):
                ttl.append(cr)
                cr=[]    
            nm.append(i)
        else:
            if (len(nm) > 0):
             # check if the numeric list is not empty and add it to final array.
                ttl.append(nm)
                nm = []
            cr.append(i)
        cnt= cnt + 1
        # to add the last array to the final array.
        if ( cnt == len(lst)):
            if(len(nm) > 0):
                ttl.append(nm)
            if (len(cr) > 0):
                ttl.append(cr)
    return ttl
# creating an array that will store all sub arrays.
fnl = []

# get input/ output files

# list of command line arguments
argumentList = sys.argv[1:]

# Options
options = "i:o:"
 
# Parsing argument
arguments, values = getopt.getopt(argumentList, options)

# checking each argument
for currentArgument, currentValue in arguments:
    if currentArgument == "-i":
        filename = currentValue
    if currentArgument == "-o":
        output = currentValue


file1 = open(output, 'w')

# read the input file and insert the sorted lines in the output file.
with open(filename, 'r') as f:
        for line in f.readlines():
            mylst = list(line.strip("\n")) # remove eol
            lt = create_partition (mylst) # create sub partitions 
            
            for cur in lt:
                string = quick_sort(cur) # sorting array
                fnl.append(''.join(string))
            fnl.append("\n") # add eol
            print (fnl) 
            file1.writelines(fnl)
            fnl = []
                
file1.close()
