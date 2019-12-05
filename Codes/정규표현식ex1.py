import re

var = input()

var2 = re.compile('the[^a-zA-Z]')
var2 = var2.findall(var)

print(len(var2)) 