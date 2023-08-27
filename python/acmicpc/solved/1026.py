n = int(input())
A = list(map(lambda x:int(x),input().split()))
B = list(map(lambda x:int(x),input().split()))

tmp_B = list(B)
res_A = [-1 for i in range(n)]

for i in range(n):
    idx_b = B.index(max(tmp_B))
    res_A[idx_b] = min(A)
    A[A.index(min(A))] = 101
    tmp_B[idx_b] = -1

tot = 0
for i in range(n):
    tot += res_A[i]*B[i]
print(tot)