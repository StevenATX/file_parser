# main.py
# Description: This script parses a text file for a customer's name containing an error.
# It uses regex to find the estimated name
# Created: Feb 26 2023
# Modified: Feb 26 2023
# Author: Steve


import re
from pprint import pprint


with open("names") as f:
    mylist = f.read().splitlines()

for item in mylist:
    #print(item)
    regexoutput = re.search("^S.*ny$",item)

    if regexoutput is not None:
        if regexoutput.group(0) is not None:
            print("Name found!")
            print(item)

