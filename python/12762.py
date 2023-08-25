def findmaxidx(L):
    imax = -1
    idx = -1
    for i in range(len(L)):
        if L[i] > imax:
            imax = L[i]
            idx = i
    return imax, idx

N = int(input())
K = list(map(int, input().split()))

L = [1]*N
before = -1
while True:
    up = False
    for i in range(1, len(K)):
        if K[i-1] > K[i]:
            if up:
                L[i] = 2
                up = False
            else:
                L[i] = L[i-1] + 1
        else:
            L[i] = L[i-1] + 1
            up = True
    print(L)
    imax, idx = findmaxidx(L)
    K.pop(idx)
    L.pop(idx)
    if imax<before:
        break
    before = imax

print(before)



'''
4 3 5 1 4 2 3

1 2 3 2 3 2 3   -> 5제거
1 2   3 4 2 3   -> 4제거
1 2   3   4 5
1 2   3   4
'''