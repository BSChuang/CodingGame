import math
xStep = 0.1
xMax = 0.4
yPrev = 0
y = 1
x = 0
while x < xMax:
    m = math.e**(x + 0.2*y)/(x + y)
    yPrev = y
    y = y + xStep*m
    x += xStep
    print(str(yPrev) + ' + ' + str(xStep) + '(' + str(m) + ') = ' '(' + str(x) + ', ' + str(y) + ')')