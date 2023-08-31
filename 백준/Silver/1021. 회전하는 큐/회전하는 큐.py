from collections import deque

N, M = map(int, input().split())

A = deque(map(int, input().split()))

cnt = 0
pop_cnt = 0
now = 1
target = A[0]

while A:
    if now == target:
        tmp = A.popleft()
        if len(A) == 0:
            break

        for i in range(len(A)):
            if tmp < A[i]: A[i] -= 1
        target = A[0]
        pop_cnt += 1
        continue

    if target > now:
        if (N-pop_cnt)-target+now < target-now:
            cnt += (N-pop_cnt)-target+now
        else:
            cnt += target-now
        
        now = target

    else:
        if (N-pop_cnt)+target-now < now-target:
            cnt += (N-pop_cnt)+target-now
        else:
            cnt += now-target

        now = target

print(cnt)