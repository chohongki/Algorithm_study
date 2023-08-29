# 이분 탐색

N = int(input())
A = list(map(int, input().split()))
M = int(input())
X = list(map(int, input().split()))

A.sort()

def find(x):
    start = 0
    end = N
    while start <= end:
        mid = (start + end) // 2
        if mid >= N:
            break
        if A[mid] < x:
            start = mid + 1
        elif A[mid] > x:
            end = mid - 1
        else :
            return 1
    return 0

for i in X:
    print(find(i))