import sys
input = sys.stdin.readline

N = int(input())

dic = {}

for i in range(1, N+1):
    u, v = map(int, input().split())
    dic[i] = [-1, -1]
    if u != -1: 
        dic[i][0] = u
    if v != -1:
        dic[i][1] = v

K = int(input())

now = 1
while True:
    left, right = dic[now]
    if left == -1 and right == -1:
        break
    elif left == -1:
        now = right
    elif right == -1:
        now = left
    else :
        if K%2 :
            now = left
            K = K//2 + 1
        else :
            now = right
            K = K//2

print(now)