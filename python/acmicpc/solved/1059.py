L = int(input())
S = map(int,input().split())
n = int(input())

max = 1001
min = 0

for i in S:
    if i>=n and i<max:
        max = i
    elif i<=n and i>min:
        min = i

if n==max or n==min:
    print("0")
else:
    print((n-min)*(max-n)-1)