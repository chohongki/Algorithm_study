T = int(input())

vps= []
flag=[]

for i in range(T):
    vps.append(input())
    flag.append(True)
    
for i in range(len(vps)):
    a = []
    for j in vps[i]:
        if j=="(" :
            a.append("(")
        elif len(a)==0:
            flag[i]=False
        else:
            a.remove("(")

    if len(a) == 0 and flag[i]==True:
        print("YES")
    else :
        print("NO")