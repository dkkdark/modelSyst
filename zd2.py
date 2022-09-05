"""
Task 2
"""

import piFun

series = 4
n_count = [10000, 100000, 1000000, 10000000, 100000000]

x0 = int(input())
y0 = int(input())
r = int(input())

Seria_1 = []
Seria_2 = []
Seria_3 = []
Seria_4 = []
Seria_5 = []

i = 0
ser1 = False
ser2 = False
ser3 = False
ser4 = False
ser5 = False

for n in n_count:
    for j in range(series):
        res = piFun.pi_count(n, x0, y0, r)
        if i < series:
            Seria_1.append(res)
        elif series <= i < series * 2:
            Seria_2.append(res)
        elif series * 2 <= i < series * 3:
            Seria_3.append(res)
        elif series * 3 <= i < series * 4:
            Seria_4.append(res)
        elif series * 4 <= i < series * 5:
            Seria_5.append(res)
        i += 1
        if len(Seria_1) == series and not ser1:
            ser1 = True
            print("Seria 1", Seria_1)
        if len(Seria_2) == series and not ser2:
            ser2 = True
            print("Seria 2", Seria_2)
        if len(Seria_3) == series and not ser3:
            ser3 = True
            print("Seria 3", Seria_3)
        if len(Seria_4) == series and not ser4:
            ser4 = True
            print("Seria 4", Seria_4)
        if len(Seria_5) == series and not ser5:
            ser5 = True
            print("Seria 5", Seria_5)

