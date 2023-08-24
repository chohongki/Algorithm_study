import sys
from collections import deque

input = sys.stdin.readline

def test():                                                                                                                              
    M, N, K = map(int, input().split())

    field = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    cnt = 0
    for i in range(N):  # y
        for j in range(M):  # x
            if field[i][j]:
                cnt += 1
                queue = deque()
                queue.append((j, i))
                while queue:
                    now = queue.popleft()
                    now_x = now[0]
                    now_y = now[1]
                    if now_x < M-1 and field[now_y][now_x+1]:
                        field[now_y][now_x+1] = 0
                        queue.append((now_x+1, now_y))
                    if now_x > 0 and field[now_y][now_x-1]:
                        field[now_y][now_x-1] = 0
                        queue.append((now_x-1, now_y))
                    if now_y < N-1 and field[now_y+1][now_x]:
                        field[now_y+1][now_x] = 0
                        queue.append((now_x, now_y+1))
                    if now_y > 0 and field[now_y-1][now_x]:
                        field[now_y-1][now_x] = 0
                        queue.append((now_x, now_y-1))
    print(cnt)

T = int(input())

for _ in range(T):
    test()