T = int(input())

lst = []

for i in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for j in range(n):
        cx, cy, r = map(int, input().split())
        d1 = (x1-cx)**2 + (y1-cy)**2
        d2 = (x2-cx)**2 + (y2-cy)**2
        if d1 < r**2 and d2 > r**2 :
            cnt += 1
        elif d1 > r**2 and d2 < r**2:
            cnt += 1
    lst.append(cnt)

print("\n".join(str(i) for i in lst))