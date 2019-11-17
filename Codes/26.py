in1, in2 = map(int, input().split())

a = set()
b = set()

for i in range(1, in1+1):
    if in1 % i == 0:
        a.add(i)

for i in range(1, in2+1):
    if in2 % i == 0:
        b.add(i)

divisor = a & b

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)