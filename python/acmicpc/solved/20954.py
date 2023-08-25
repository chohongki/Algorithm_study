import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    exp = 0
    while 2**exp < abs(n): exp += 1
    if n==0: res = 0
    elif n>0 : res = 4* 2**exp -4 + n
    else : res = 4*2**exp -4 + 2**(exp+1) - n
    print(res)