"""
Find pi function
"""

import random


def pi_count(n, x0, y0, r):
    xMax = x0 + r
    xMin = x0 - r
    yMax = y0 + r
    yMin = y0 - r

    m = 0

    for i in range(n):
        p = random.uniform(0, 1)
        xp = (xMax - xMin) * p + xMin
        p = random.uniform(0, 1)
        yp = (yMax - yMin) * p + yMin
        if (xp - x0) ** 2 + (yp - y0) ** 2 < r ** 2:
            m += 1

    pi = 4 * m / n
    return pi