var = list(input().split(";"))

var = list(map(int, var))
var.sort(reverse=True)

for i in range(0, len(var)):
    var[i] = '{0:>9,}'.format(var[i], ",")
    print(var[i])
