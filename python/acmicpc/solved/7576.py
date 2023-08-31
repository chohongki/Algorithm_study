# BFS

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

queue = deque()
for col in range(len(box)):
    for row in range(len(box[col])):
        if box[col][row] == 1:
            queue.append((col, row))
            cnt += 1
        elif box[col][row] == -1:
            cnt += 1

def add_queue(col, row):
    if 0 <= col <= N-1 and 0 <= row <= M-1:
        if box[col][row] == 0:
            box[col][row] = 1
            queue.append((col, row))
            return True
        elif box[col][row] == -1:
            return False
    return False

day = -1
while True:
    day += 1
    flag = False
    copy_queue = queue.copy()
    queue = deque()
    while copy_queue:
        now_col, now_row = copy_queue.popleft()

        if add_queue(now_col-1, now_row):
            cnt += 1
            flag = True
        if add_queue(now_col+1, now_row):
            cnt += 1
            flag = True
        if add_queue(now_col, now_row-1):
            cnt += 1
            flag = True
        if add_queue(now_col, now_row+1):
            cnt += 1
            flag = True

    if flag==False:
        break

if cnt < M*N:
    print(-1)
else:
    print(day)

