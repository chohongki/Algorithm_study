# 분할 정복을 이용한 거듭제곱

A, B, C = map(int,input().split())

def a(base, idx, mod):
    if idx == 1:
        return base % mod
    elif idx % 2:
        return (base * a(base, idx-1, mod)) % mod
    else :
        tmp = a(base, idx/2, mod)
        return (tmp * tmp) % mod

print(a(A, B, C))