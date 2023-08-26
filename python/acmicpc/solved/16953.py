A, B = map(int,input().split())

cnt = 1
flag = True

while B > A and flag == True:
    
    if B % 2 == 0:
        cnt+=1
        B /= 2
    elif B % 10 == 1:
        cnt+=1
        B = int(B//10)
    else :
        flag = False
    if B < A:
        flag = False
    

if flag:
    print(cnt)
else :
    print(-1)