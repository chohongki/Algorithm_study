N, K = map(int, input().split())
A = [0]*N
for i in range(N):
    A[i] = int(input())
s = 0
for i in A[::-1]:
    if K>=i:
        s += K//i
        K -= i* (K//i)

print(s)