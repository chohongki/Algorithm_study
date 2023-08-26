import sys
input = sys.stdin.readline

n = int(input())

tree = [[]]*n
for i in range(n):
    tree[i] = list(map(int, input().split()))

s = []+tree

for i in range((n-1) -1, -1, -1):
    for j in range(i+1):
        s[i][j] = tree[i][j] + max(s[i+1][j], s[i+1][j+1])

print(s[0][0])