import sys
input = sys.stdin.readline

n, k, x = map(int, input().split())

member = []

for _ in range(n):
    a = int(input().split()[0])
    member.append(a)

member.sort()

i = 0
min = 9999999999

DP = [0 for i in range(n+1)]

while True:
    tmp = sum(member[i:i+k])
    if abs(x*k/2 - tmp) < min:
        min = abs(x*k/2 - tmp)
        i += 1

    else :
        break

print(-min**2 + (x*k/2)**2)

'''
(a1 + a2 + a3 + a4)*(x*k - a1 - a2 - a3 - a4)

능력치 식 : x*k*(a1 + a2 + a3 + a4) - (a1 + a2 + a3 + a4)**2

(a1 + a2 + a3 + a4) = t

-t**2 + xkt
-(t-xk/2)**2 + (xk/2)**2

t-xk/2가 최소값 되는 t = (a1 + a2 + a3 + a4)


a1~an n개의 수 k개의 숫자를 여기서 선택해서
k개의 숫자의 합산이 특정 값(xk/2)에 가까워져야함

or 

능력치 최대값 구하기


만약 t-xk/2가 이전보다 작음 : 갱신
만약 t-xk/2가 이전보다 큼 : 이전 최적값에다가 
'''