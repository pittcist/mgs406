import sys

with open('NYSE_DATA_SHUFFLE.txt', 'r') as fr:
    lines = fr.readlines()

# initialize the variables, lastKey with None and maxValue with 0
(lastKey, maxValue) = (None, 0)
# print(lastKey, maxValue)

# values produced by the mapper are read by STDIN (standard input) and do
# the following for each input line (loop)
for line in lines:

#     remove leading and trailing whitespace
    line = line.strip()
    # print(line)
#     line is split by tab, that was used in the printing of the result by
#     the mapper, and assigned to key and value respectively
    (key, value)= line.split(',')
    # print(key,value)

#     if lastKey is defined and it is not equal to key of input line,
#     print last key and maxValue and assign key to the
#     lastKey and maxValue to the value of input line

    if lastKey and lastKey != key:
        # print('%s\t%s' % (lastKey, maxValue))
        (lastKey, maxValue) = (key, int(value))

#     else (if lastKey is defined and equal to key) lastKey takes
#    the value of key and maxValue is assigned to the maximum
#     between the current maxValue and the value of that key
    else:
        (lastKey, maxValue) = (key, max(maxValue, int(value)))

    # print(lastKey,maxValue)
# loop for lines of input ends

# # print lastKey and maxValue if lastKey is defined
if lastKey:
    print('%s\t%s' % (lastKey, maxValue))









