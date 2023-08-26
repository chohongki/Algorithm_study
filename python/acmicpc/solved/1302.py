n = int(input())

d = {}

for i in range(n):
    a = input()
    if a in d:    
        d[a] = d[a] + 1
    else :
        d[a] = 1

d = dict(sorted(d.items(), key=lambda x: x[0]))

max_key = max(d, key=d.get)

print(max_key)