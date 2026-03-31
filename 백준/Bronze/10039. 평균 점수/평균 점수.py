sum = 0
for i in range(5):
	p=int(input())
	if p<40 :
		p=40
	sum+=p
print(int(sum/5))