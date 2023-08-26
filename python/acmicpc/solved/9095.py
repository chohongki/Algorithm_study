case = [i for i in range(12)]
case[3] = 4

def test(n):
    if n >= 4:
        case[n] = test(n-3)+test(n-2)+test(n-1)
    return case[n]
    
T = int(input())
test(11)
for i in range(T):
    n=int(input())
    print(case[n])