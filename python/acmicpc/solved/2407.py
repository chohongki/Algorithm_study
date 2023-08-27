from math import factorial

n, m = map(int, input().split())

if m < n/2 :
    m = n-m

res = 1
for i in range(m+1, n+1):
    res *= i

print(res//factorial(n-m))