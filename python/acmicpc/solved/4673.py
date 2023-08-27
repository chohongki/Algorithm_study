def n(num):
    sum = num
    a = num
    
    while a >= 10 :
        a, b = divmod(a, 10)
        sum += b
    return sum + a

list = [False for i in range(9999+9+9+9+9)]
list[1] = True
print(1)
for i in range(2, 10001):
    list[n(i)-1] = True
    if list[i-1] == False:
        print(i)