file = "level1_5.in"
output = file + ".txt"
f = open(file, "r")
out = open(output, "a")
number = int(f.readline())
print(number)
for x in f:
    nW = 0
    nS = 0
    nA = 0
    nD = 0
    for i in x:
        if i == 'D':
            nD += 1
        elif i == 'A':
            nA += 1
        elif i == 'S':
            nS += 1
        elif i == 'W':
            nW += 1
    res = str(nW) + " " + str(nD) + " " + str(nS) + " " + str(nA) + "\n"
    out.write(res)

