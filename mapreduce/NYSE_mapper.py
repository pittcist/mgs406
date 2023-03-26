import sys

with open('mapreduce/NYSE_DATA.txt', 'r') as fr:
    lines = fr.readlines()

# maplines = []

with open('mapreduce/NYSE_DATA_MAP.txt', 'w') as fw:
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
