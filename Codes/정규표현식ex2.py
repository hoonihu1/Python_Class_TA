import csv
import re

a = ''

with open('../Input_Folder/python_input.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        a += ''.join(row)

p = re.compile('\d{3}-\d{4}-\d{4}')
l = re.compile('\d{3}-\d{4}-\d{4}|\d{3}-\d{3}-\d{4}')
n = re.compile('\d{3}\.\d{4}\.\d{4}')
m = p.findall(a)
k = l.findall(a)
g = n.findall(a)

print(m)
print(k)
print(g)