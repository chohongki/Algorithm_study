import sys
sys.setrecursionlimit(10000)

N = int(input())
minimum = [[-1]*3]*(N+1)
price = [[0,0,0]]

for i in range(N):
    price.append(list(map(int, input().split())))

minimum = price[:]

def a(n):
    if n == 1 : return minimum[1]
    else: 
        temp = a(n-1)
        for i in range(3):
            minimum[n][i] = min(temp[:i]+temp[i+1:]) + price[n][i]
        return minimum[n]

print(min(a(N)))