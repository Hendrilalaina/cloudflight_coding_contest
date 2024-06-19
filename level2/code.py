file = "level2_5.in"
output = file + ".txt"
f = open(file, "r")
out = open(output, "a")
number = int(f.readline())
print(number)
for f1 in f:
    x = 0
    y = 0
    xMin, xMax = [0, 0]
    yMin, yMax = [0, 0]
    for i in f1:
        if i == 'D':
            x += 1
            xMax = max(x, xMax)
        elif i == 'A':
            x -= 1
            xMin = min(x, xMin)
        elif i == 'W':
            y += 1
            yMax = max(y, yMax)
        elif i == 'S':
            y -= 1
            yMin = min(y, yMin)
    res =  str(xMax - xMin + 1) + " " + str(yMax - yMin + 1) + "\n"
    out.write(res)