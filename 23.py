col, row = map(int, input().split())

matrix = []

for i in range(row):
    matrix.append(list(input()))

row = row - 1
col = col - 1

for i in range(0, row+1):
    for j in range(0, col+1):
        if matrix[i][j] == '.':
            count = 0
            if i+1 <= row and matrix[i+1][j] == '*':
                count = count + 1
            if j+1 <= col and matrix[i][j+1] == '*':
                count = count + 1
            if i-1 >= 0 and matrix[i-1][j] == '*':
                count = count + 1
            if j-1 >= 0 and matrix[i][j-1] == '*':
                count = count + 1
            if i-1 >= 0 and j-1 >= 0 and matrix[i-1][j-1] == '*':
                count = count + 1
            if i+1 <= row and j+1 <= col and matrix[i+1][j+1] == '*':
                count = count + 1
            if i-1 >= 0 and j+1 <= col and matrix[i - 1][j + 1] == '*':
                count = count + 1
            if i+1 <= row and j-1 >= 0 and matrix[i + 1][j - 1] == '*':
                count = count + 1
            matrix[i][j] = count
        else:
            continue

for i in range(0, row+1):
    for j in range(0, col+1):
        print(matrix[i][j], end="")
    print()