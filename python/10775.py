import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
airplane = [int(input()) for _ in range(P)]
gate = [i for i in range(1, G+1)]

for i in range(1, P+1):
    if i > G:
        break
    
