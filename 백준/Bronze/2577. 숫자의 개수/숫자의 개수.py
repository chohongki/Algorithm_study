a=int(input())*int(input())*int(input())
a=str(a)
for i in range(10):
    cnt=0
    for j in a:
        if i==int(j):
            cnt+=1
    print(cnt)