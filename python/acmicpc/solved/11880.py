import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b, c = map(int, input().split())
    print(min((a+b)**2+c**2, (a+c)**2+b**2, (b+c)**2+a**2))