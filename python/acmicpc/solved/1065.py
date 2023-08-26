N = int(input())

if N<=99 :
    cnt = N

else :
    cnt = 99
    for i in range(100, N+1):
        if ((i//100) - (i//10)%10) == ((i//10)%10 - i%10):
            cnt+=1

print(cnt)      
