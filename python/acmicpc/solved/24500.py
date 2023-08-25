N = int(input())

K = 1

while K < N: K = 2 * K + 1

if K == N:
    print(1)
    print(K)
else:
    print(2)
    print(K ^ N)
    print(N)
