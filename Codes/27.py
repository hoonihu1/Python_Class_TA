file = open('words.txt', 'r')

s = file.read().split()

for i in range(0, len(s)):
    s[i] = s[i].rstrip(',.')

result = [r for r in s if "c" in r]

for i in result:
    print(i)

file.close()