# 에라토스테네스의 체

N = int(input())
numbers = list(map(lambda x: int(x),input().split()))

primeArr = [True for i in range(1001)]
primeArr[0] = False
primeArr[1] = False

for i in range(2, int(1000**0.5)+1):
    for j in range(i*2, 1001, i):
        primeArr[j] = False

cnt = 0
for i in numbers:

    if primeArr[i] == True:
        cnt+=1

print(cnt)

