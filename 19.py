input = int(input())

for i in range(1, input+1):
    for j in range(1, input-i+1):
        print(" ",end="")

    for k in range(1, 2*i):
        print("*",end="")

    print()