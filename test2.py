import re

p = re.compile('[a-z]+') # 소문자(a-z)가 1회 이상 반복되는 걸 찾아와라.
m = p.findall("Python is so easy!")
print(m)
print(type(m)) # m의 타입은!?

