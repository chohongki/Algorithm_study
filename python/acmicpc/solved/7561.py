import sys
import copy

def det(A):
    return (A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1])
            - A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0])
            + A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0]))

def makeAi(A, B, i):
    Ai = copy.deepcopy(A)
    for j in range(3):
        Ai[j][i] = B[j]
    return det(Ai)

def test():
    A = []
    B = []
    x = []
    for _ in range(3):
        a1, a2, a3, b = map(int, sys.stdin.readline().split())
        A.append([a1, a2, a3])
        B.append(b)
    for i in range(3):
        x.append(makeAi(A,B,i))
    x.append(det(A))
    print(" ".join(map(str, x)))
    if x[3] == 0:
        print("No unique solution")
    else:
        print("Unique solution: ", end="")
        res = [x[0]/x[3], x[1]/x[3], x[2]/x[3]]
        for i in range(len(res)):
            if -0.0005<res[i]<0.0005:
                res[i] = 0
        print("{0:0.3f} {1:0.3f} {2:0.3f}".format(res[0], res[1], res[2]))

T = int(sys.stdin.readline())
for _ in range(T):
    test()
    print()
