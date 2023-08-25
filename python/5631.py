import sys
input = sys.stdin.readline

N = int(input())

home = []
for _ in range(N):
    home.append(list(map(int, input().split())))

ax, ay, bx, by, q = map(int, input().split())

R = []
for _ in range(q):
    R.append(list(map(int, input().split())))
input()

