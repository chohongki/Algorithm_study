# dijikstra
import heapq


INF = 100000

N, K = map(int, input().split())

queue = []
heapq.heappush(queue, (0, N))

distance = [INF] * (100001)
distance[N] = 0

prev = INF

while queue:
    now_cnt, now_pos = heapq.heappop(queue)

    if now_pos == K:
        break
    
    if distance[now_pos] <  now_cnt:
        continue

    if now_pos > 0 and now_cnt + 1 < distance[now_pos - 1]:
        distance[now_pos - 1] = now_cnt + 1
        heapq.heappush(queue, (now_cnt+1, now_pos-1))
    if now_pos < 100000 and now_cnt + 1 < distance[now_pos + 1]:
        distance[now_pos + 1] = now_cnt + 1
        heapq.heappush(queue, (now_cnt+1, now_pos+1))
    if now_pos * 2 < 100001 and now_cnt < distance[now_pos * 2]:
        distance[now_pos * 2] = now_cnt
        heapq.heappush(queue, (now_cnt, now_pos*2))

print(distance[K])