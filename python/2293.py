import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

arr = [0 for _ in range(k+1)]
coins.sort(reverse=True)

for i in range(0, k+1, k//coins[0]):
    arr[i] == 1

for price in coins[1:]:
    arr[0] += 1
    for idx in range(price, k//price + 1):
        arr[idx] = arr[idx-price]
        if idx%price == 0: arr[idx] += 1
print(arr)