import sys
input = sys.stdin.readline

N, M = map(int, input().split())
know_list = list(map(int, input().split()))[1:]

partys = [[] for _ in range(M+1)]
peopleInParty = [[] for _ in range(N+1)]


for i in range(1, M+1):
    partys[i] = list(map(int, input().split()))[1:]
    for j in partys[i]:
        peopleInParty[j].append(i)

queue = []
for i in know_list:
    queue.extend(peopleInParty[i])
queue = list(set(queue))

visitedParty = []

while queue:
    n = queue.pop()
    if n in visitedParty: continue
    visitedParty.append(n)
    for i in partys[n]:
        queue.extend(peopleInParty[i])
    queue = list(set(queue))

print(M-len(visitedParty))
