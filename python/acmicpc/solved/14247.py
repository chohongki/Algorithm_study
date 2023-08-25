import sys
input = sys.stdin.readline

n = int(input())

arr = list(zip(list(map(int, input().split())), list(map(int, input().split()))))
arr.sort(key = lambda x:x[1])
res = 0

for i in range(n):
    res += arr[i][0] + arr[i][1]*i
print(res)
    
