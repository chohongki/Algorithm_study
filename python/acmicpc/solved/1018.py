# B = 0   W = 1
def counting(tmp, flag):
    cnt=0
    for a in range(8):
        for b in range(8):
            if (tmp[a][b] == "B" and flag == 1) or (tmp[a][b] == "W" and flag == 0):
                cnt+=1
            flag = 1-flag
        flag = 1-flag
    return cnt if cnt<32 else 64-cnt

n,m = map(int,input().split())
lst = [0]*n
min=999999

for i in range(n):
    lst[i] = input()

tmp = [0]*8
for j in range(m-7):
    for i in range(n-7):
        for k in range(8):
            tmp[k]=lst[k+i][j:j+8]
        cnt = counting(tmp, 0)
        min = min if min<cnt else cnt
print(min)
