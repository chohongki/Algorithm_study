N = int(input())

points = []


for _ in range(N):
    x, y = map(int, input().split())

    points.append((x, y))


sum = 0
prev_x, prev_y = points[-1]
for x, y in points:
    sum += prev_x*y - x*prev_y
    prev_x = x
    prev_y = y

sum = abs(sum)
sum *= 0.5

print("%.1f" % sum)