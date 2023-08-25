# 타일링 문제이지만 좀만 생각해보면 피보나치 문제

n = int(input())

arr = [0 for _ in range(n+1)]
arr[0] = arr[1] = 1

for i in range(2, n+1):
    arr[i] = (arr[i-1] + arr[i-2]) % 10007

print(arr[-1])