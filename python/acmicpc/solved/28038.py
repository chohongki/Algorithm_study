import sys
import math
input = sys.stdin.readline

def test():
    c = int(input())
    a, b = map(float, input().split())
    if c == 1:
        r = round(math.sqrt(a**2+b**2),8)
        theta = math.atan2(b,a)
        if theta < 0:
            theta = 2* math.pi + theta
        theta = round(theta, 8)
        if r.is_integer(): r = int(r)
        if theta.is_integer(): theta = int(theta)
        print(r, end=' ')
        print(theta)

    else:
        x = round(a * math.cos(b),8)
        y = round(a * math.sin(b),8)
        if x.is_integer(): x = int(x)
        if y.is_integer(): y = int(y)
        print(x, end=' ')
        print(y)


T = int(input())

for _ in range(T):
    test()