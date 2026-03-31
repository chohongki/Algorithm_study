x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

a = x1*y2 + x2*y3 + x3*y1
b = y1*x2 + y2*x3 + y3*x1

if a==b:
    print(0)
elif a>b:
    print(1)
else :
    print(-1)