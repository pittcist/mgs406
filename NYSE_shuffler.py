import sys

with open('NYSE_DATA_MAP.txt', 'r') as fr:
    lines = fr.readlines()

sorted_lines = sorted(lines)
# print(sorted_lines)


with open('NYSE_DATA_SHUFFLE.txt', 'w') as fw:
    fw.writelines(sorted_lines)  
