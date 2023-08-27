import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

queue = deque()
for _ in range(N):
    command = input().split()
    if len(command) == 1:
        if command[0] == "pop":
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        if command[0] == "size":
            print(len(queue))
        if command[0] == "empty":
            print(0 if queue else 1)
        if command[0] == "front":
            if queue:
                print(queue[0])
            else:
                print(-1)
        if command[0] == "back":
            if queue:
                print(queue[-1])
            else:
                print(-1)
    else:
        queue.append(int(command[1]))