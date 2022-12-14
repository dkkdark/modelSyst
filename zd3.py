"""
Task 3
"""

import piFun, math

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


# Count error. Code above is the save as in zd2

average1 = sum(Seria_1) / len(Seria_1)
average2 = sum(Seria_2) / len(Seria_2)
average3 = sum(Seria_3) / len(Seria_3)
average4 = sum(Seria_4) / len(Seria_4)
average5 = sum(Seria_5) / len(Seria_5)

average = (average1 + average2 + average3 + average4 + average5) / 5

average1_error = (average1 - math.pi) / math.pi
average2_error = (average2 - math.pi) / math.pi
average3_error = (average3 - math.pi) / math.pi
average4_error = (average4 - math.pi) / math.pi
average5_error = (average5 - math.pi) / math.pi
average_error = (average - math.pi) / math.pi
print("Average Error 1: ", average1_error)
print("Average Error 2: ", average2_error)
print("Average Error 3: ", average3_error)
print("Average Error 4: ", average4_error)
print("Average Error 5: ", average5_error)
print("Average Error: ", average_error)

