A = int(input())
T = int(input())
tp = int(input())

start = 0
L = 0
i = 1
while True:
    i += 1
    L = 4 + 2*i
    if T <= L/2:
        if T <=2:
            print((start + 2*(T-1)+ tp)%A)
            break
        else:
            print((start + 4 + i*tp + (T-3))%A)
            break
    start = (start + L%A) % A
    T -= L//2