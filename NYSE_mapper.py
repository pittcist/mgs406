#!/usr/bin/env python
# this line means that the script is executable,
# it calls the language interpreter to run the code inside the script
# and is the guide to find 'python'


# import the module for reading and writing data
import sys

# input is read by STDIN (standard input) and do the following for each
# input line

with open('NYSE_DATA.txt', 'r') as fr:
    lines = fr.readlines()

# maplines = []

with open('NYSE_DATA_MAP.txt', 'w') as fw:
    for line in lines:
        # print(line)

        # remove leading and trailing whitespace
        line = line.strip()

        # split the line by comma separator, a list is produced
        line = line.split(",")

        # assign first value of the list to the ticker
        ticker = line[0]

        # assign the third value to the trade price
        tradePrice = line[2]

        # mapper prints ticker and trade price with a tab in between, which is
        # taken as input by the reducer
        # print ('{0}, {1}'.format(ticker, tradePrice))
        # maplines.append([ticker, tradePrice])

        fw.write('{0},{1}\n'.format(ticker, tradePrice))
