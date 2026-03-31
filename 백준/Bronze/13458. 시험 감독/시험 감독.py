n=int(input())
a=list(map(int,input().split()))
b,c = map(int,input().split())
cnt=0
for i in range(n):
	t=a[i]
	cnt+=1
	t-=b
	if(t>=0):
		cnt+=int(t/c)
	if(t>=0 and t%c != 0):
		cnt+=1

print(cnt)