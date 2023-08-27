def a(n):
    if n==0:
        return 0
    return n%2 + a(n//2)

start = 64
X = int(input())
print(a(X))