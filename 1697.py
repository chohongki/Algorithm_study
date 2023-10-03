# dijikstra
from collections import deque, Counter


INF = 100000

N, K = map(int, input().split())

fastest = INF

queue = []
queue.append((0, N))

distance = [INF] * (100001)
distance[N] = 0

reached = []

prev = INF

while queue:
    now_cnt, now_pos = queue.pop()
    
    if distance[now_pos] <  now_cnt or now_cnt > fastest:
        continue

    if now_pos*2 > 100000:
        continue

    if now_pos == K:
        reached.append(now_cnt+1)
        if now_cnt < fastest:
            fastest = now_cnt
        continue
    
    if now_pos > 0 and now_cnt + 1 <= distance[now_pos - 1]:
        distance[now_pos - 1] = now_cnt + 1
        queue.append((now_cnt+1, now_pos-1))
    if now_pos < K and now_cnt + 1 <= distance[now_pos + 1]:
        distance[now_pos + 1] = now_cnt + 1
        queue.append((now_cnt+1, now_pos+1))
    if now_pos <= K and now_cnt + 1 <= distance[now_pos * 2]:
        distance[now_pos * 2] = now_cnt + 1
        queue.append((now_cnt+1, now_pos*2))

print(distance[K])
cnt_dict = Counter(reached)
print(cnt_dict[min(cnt_dict.keys())])