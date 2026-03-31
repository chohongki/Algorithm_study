import math

n = int(input())
for i in range(n):
	x1,y1,r1,x2,y2,r2 = map(int,input().split())
	if x1==x2 and y1==y2:
	    if r1==r2:
	        print('-1')
	    else :
	        print('0')
	else :
	    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
	    r12 = r1+r2
	    if d>r12:
	        print('0')
	    elif d<r12:
	        r21 = abs(r1-r2)
	        if r21>d:
	            print('0')
	        elif r21<d:
	            print('2')
	        else : 
	            print('1')
	    else :
	        print('1')