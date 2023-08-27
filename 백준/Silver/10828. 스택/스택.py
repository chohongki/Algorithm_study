import sys
input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    command = input().split()
    if len(command) == 1:
        if command[0] == "pop":
            try:
                print(stack.pop())
            except:
                print(-1)
        if command[0] == "size":
            print(len(stack))
        if command[0] == "empty":
            print(0 if stack else 1)
        if command[0] == "top":
            try:
                print(stack[-1])
            except:
                print(-1)
    else:
        stack.append(int(command[1]))