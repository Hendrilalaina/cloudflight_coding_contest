file = "level3_example.in"
output = file + ".txt"
f = open(file, "r")
out = open(output, "a")
number = int(f.readline())

x, y = f.readline().split()
x = int(x)
y = int(y)
# print(x)
# print(y)
l = [[0]*x]*y
for i in range(y):
    s = f.readline().split()
    for j in range(x):
        l[i][j] = s[j]
        # if s[j] == '.':
        #     print(0)
        # elif s[j] == 'X':
        #     print(1)
print(l)