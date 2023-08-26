a = int(input())
m = [0 for i in range(a + 1)]

for i in range(2, a+1):
    m[i] = m[i-1]+1
    if i%3 == 0 :
        m[i] = min(m[i//3]+1, m[i])
    if i%2 == 0 :
        m[i] = min(m[i//2]+1, m[i])

print(m[a])