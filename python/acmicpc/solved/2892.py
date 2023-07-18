def hextoint(x):
    return int("0x"+x,16)

N = int(input())
K = list(map(hextoint, input().split()))

res = ""
for i in K:
    flag = False
    for j in range(10):
        if 97<=i^ord(str(j))<=122:
            flag = True
            break
    if flag:
        res+="-"
    else:
        res+="."
print(res)