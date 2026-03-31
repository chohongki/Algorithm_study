n = int(input())
sum=0
l = list(map(int,input().split()))
m = max(l)
for i in l:
	sum+=(i*100/m)
print("%0.2f" %(sum/n))