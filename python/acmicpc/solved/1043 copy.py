# 집합(set) 이용한 풀이

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
know_list = set(input().split()[1:])

parties = []

for i in range(M):
    parties.append(set(input().split()[1:]))

for _ in range(M):
    for i in parties:
        if i & know_list:
            know_list = know_list.union(i)
    print(know_list)

cnt = 0

for i in parties:
    if i & know_list: continue
    cnt += 1

print(cnt)