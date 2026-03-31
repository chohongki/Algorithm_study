n=input()
for i in range(n):
    a=0
    b=1
    d=input()
    if d==0:
        print 1,0
    elif d==1:
        print 0,1
    else:
        for i in range(d-1):
            c=b
            b=b+a
            a=c
            
        print a,b
        