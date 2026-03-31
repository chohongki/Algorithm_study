list=[]
n=int(input())
for i in range(n):
	list.append(int(input()))

for i in range(n-1,0,-1):
	for j in range(i):
		if list[j]>list[j+1]:
			list[j],list[j+1]=list[j+1],list[j]

for i in list:
	print(i)