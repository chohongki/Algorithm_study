import sys

N = int(sys.stdin.readline())

K = [[0, 0]]*N

for i in range(N):
    start, end, people = map(int, sys.stdin.readline().split())
    if i == 0 or i == 1:
        K[i] = [end, people]
        continue
    else:
        K[i] = [end, max(people + K[i-3][1], people + K[i-2][1], K[i][1])]
print(max(i[1] for i in K))
    
    
    
