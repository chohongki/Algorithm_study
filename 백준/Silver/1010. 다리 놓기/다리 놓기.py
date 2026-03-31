n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    if a<b:
        a,b=b,a
    
    s1=1
    s2=1
    tmp=b
    for i in range(tmp):
        s1*=a
        a-=1
        s2*=b
        b-=1
    print(s1//s2)

    
