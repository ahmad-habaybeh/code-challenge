'''
This Python code was written in code challenge to rotate an ASCII image in text file
and insert the output in another file.

By: Ahmad Habaybeh
08/06/2022

'''

import os
import numpy as np
import getopt
import sys

filename = "myinput.txt"
outfile = "my-outputs.txt"

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
        outfile = currentValue

# function to fill an array with extra items to match other arrays.
def fillarray(num, arry):
    while (len(arry) <= num):
        arry.append("")
# initializing varaiables
array2D = []
lent = 0

# reading the input file into an array
with open(filename, 'r') as f:
        for line in f.readlines():
            array2D.append(line.strip("\n"))

# converting the array to array of arrays
for i,x in enumerate(array2D):
    array2D[i] = list (x)
    
# get the largest array lenght
for i,x in enumerate(array2D):
    if (len(array2D[i]) >= lent):
        lent = len(array2D[i])
# adding extra items to short arrays in order to match the longest line from the file
# and having an even lengths arrays 
for i,x in enumerate(array2D):
    fillarray(lent, array2D[i])

# convert the array to numpy array to use numpy function on it.
nparr = np.array(array2D)

# rotate the numpy array 90 degrees.
farr1 = np.rot90(nparr)
farr2 = np.rot90(farr1)
farr3 = np.rot90(farr2)
farr4 =np.flip(farr3, 1)

# open a file in write mode
file = open(outfile, "w")
# save final array to the file
for i in farr4:
    for x in i:
        file.write(str(x))
    file.write("\n")

# close the file
file.close()

