n=int(input())

s5=int(n/5)
n%=5
while True:
	s3=int(n/3)
	n%=3
	if n is not 0:
		n+=(s3*3+5)
		s5-=1
		if s5<0: 
			res=-1
			break;
	else :
		res=s5+s3
		break;
print(res)