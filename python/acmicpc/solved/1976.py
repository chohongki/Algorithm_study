import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

d = {i:[] for i in range(1, N+1)}

for i in range(1, N+1):
    tmp = list(map(int,input().split()))
    for j in range(1, N+1):
        if tmp[j-1] and j not in d[i]:
            d[i].append(j)
            d[j].append(i)

toVisit = list(map(int, input().split()))

def travel(toVisit):
    visited = set([toVisit[0]])
    queue = []
    queue.append(toVisit[0])
    while queue:
        now = queue.pop(-1)
        visited.add(now)
        queue.extend(set(d[now])-visited)
    flag = True
    for i in toVisit:
        if i not in visited:
            flag=False        
    return flag

if travel(toVisit):
    print("YES")
else:
    print("NO")