"""
Task 4
"""

import random

n = [10000, 100000, 1000000, 10000000]
series = 3
result = 6

seria_1 = []
seria_2 = []
seria_3 = []
seria_4 = []

xMin = 0
xMax = 2
yMin = 0
yMax = 9


def integral_count(n_count):
    m = 0
    for i in range(n_count):
        i += 1
        p = random.uniform(0, 1)
        xp = (xMax - xMin) * p + xMin
        p = random.uniform(0, 1)
        yp = (yMax - yMin) * p + yMin

        if xp ** 3 + 1 > yp:
            m += 1

    sum = 2 * 9 * m / n_count
    return sum


ii = 0
ser1 = False
ser2 = False
ser3 = False
ser4 = False

for i in n:
    for j in range(series):
        res = integral_count(i)
        if ii < series:
            seria_1.append(res)
        elif series <= ii < series * 2:
            seria_2.append(res)
        elif series * 2 <= ii < series * 3:
            seria_3.append(res)
        elif series * 3 <= ii < series * 4:
            seria_4.append(res)
        ii += 1
        if len(seria_1) == series and not ser1:
            ser1 = True
            print("Seria 1", seria_1)
        if len(seria_2) == series and not ser2:
            ser2 = True
            print("Seria 2", seria_2)
        if len(seria_3) == series and not ser3:
            ser3 = True
            print("Seria 3", seria_3)
        if len(seria_4) == series and not ser4:
            ser4 = True
            print("Seria 4", seria_4)


average1 = sum(seria_1) / len(seria_1)
average2 = sum(seria_2) / len(seria_2)
average3 = sum(seria_3) / len(seria_3)
average4 = sum(seria_4) / len(seria_4)

error1 = (average1 - result) / result
error2 = (average2 - result) / result
error3 = (average3 - result) / result
error4 = (average4 - result) / result

print("Error 1: ", error1)
print("Error 2: ", error2)
print("Error 3: ", error3)
print("Error 4: ", error4)
