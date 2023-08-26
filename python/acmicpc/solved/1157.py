n = input().upper()
cnt = 0
lst = [0]*26
flag=0
for i in n:
    lst[int(ord(i))-65]+=1

mx = max(lst)
for i in lst:
    if mx==i:
        flag+=1

if flag > 1 :
    print('?')
else:    
    print(chr(lst.index(mx)+65))
