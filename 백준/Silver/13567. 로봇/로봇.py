def move(a,to,pos,FLAG):
	if(to==0):
		if(pos[0]+a>m):
			return pos,1
		else :
			pos[0]+=a
			return pos,FLAG
	elif(to==1):
		if(pos[1]+a>m):
			return pos,1
		else :
			pos[1]+=a
			return pos,FLAG
	elif(to==2):
		if(pos[0]-a<0):
			return pos,1
		else :
			pos[0]-=a
			return pos,FLAG
	else :
		if(pos[1]-a<0):
			return pos,1
		else :
			pos[1]-=a
			return pos,FLAG



pos=[0,0]
to=0
FLAG=0
m,n=map(int,input().split())
for i in range(n):
	tp,a=list(input().split())
	a=int(a)
	if(tp=="MOVE"):
		pos,FLAG=move(a,to,pos,FLAG)
	else:
		if(a==0):
			to+=1
			to%=4
		else:
			to-=1
			to%=4

if FLAG==0 :
	print(pos[0],pos[1])
else :
	print("-1")