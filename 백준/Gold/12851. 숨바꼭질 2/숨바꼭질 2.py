from collections import Counter, deque


INF = 100000

N, K = map(int, input().split())

queue = deque()
queue.append((0, N))

visited = []

distance = [INF] * (100001)
distance[N] = 0

while queue:
    now_cnt, now_pos = queue.pop()

    if now_pos == K:
        visited.append(now_cnt)
        continue
    
    if distance[now_pos] <  now_cnt:
        continue

    next_cnt = now_cnt + 1
    if now_pos > 0 and next_cnt <= distance[now_pos - 1]:
        distance[now_pos - 1] = next_cnt
        queue.append((next_cnt, now_pos-1))
    if now_pos < 100000 and next_cnt <= distance[now_pos + 1]:
        distance[now_pos + 1] = next_cnt
        queue.append((next_cnt, now_pos+1))
    if now_pos * 2 < 100001 and next_cnt <= distance[now_pos * 2]:
        distance[now_pos * 2] = next_cnt
        queue.appendleft((next_cnt, now_pos*2))

print(distance[K])
tmp = Counter(visited)
print(tmp[min(tmp.keys())])