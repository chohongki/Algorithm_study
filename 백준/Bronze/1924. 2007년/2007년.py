x,y=map(int,input().split())
days=[31,28,31,30,31,30,31,31,30,31,30,31]
week=["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
sum=y
for i in range(x-1):
	sum+=days[i]
print(week[sum%7])