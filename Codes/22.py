n, m = map(int, input().split())

list = []

for i in range(n, m+1) :
    if i !=2 and i!= m-1 :
        list = list + [2**i]

print (list)