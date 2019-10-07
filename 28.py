file = open('words2.txt', 'r')

s = file.read().split()

for i in s:
    if list(i) == list(reversed(i)):
        print(i)

file.close()