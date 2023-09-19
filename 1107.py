N = input()
M = int(input())
if M:
    broken = list(map(int, input().split()))
able = list(set(range(10)) - set(broken))

if M==10:
    print(abs(int(N)-100))
elif M==0:
    print(min(abs(int(N)-100), len(N)))
else :
    N_able = list(N)
    for i in range(len(N)):
        min_value = 10
        for j in able:
            if abs(int(N[i]) - j) < min_value:
                min_value = abs(int(N[i]) - j)
                N_able[i] = str(j)
    print("".join(N_able))
    print(min(abs(int(N)-100), abs(int("".join(N_able))-int(N))+len(N)))

