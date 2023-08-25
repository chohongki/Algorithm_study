import sys
input = sys.stdin.readline

def test(n):
    int_part, frac_part  = n.split('.')
    non_repeat, repeat =  frac_part.split('(')
    int_part = int(int_part)
    repeat_numer = repeat[:-2]

    if repeat_numer == '':
        non_repeat_numer = int(non_repeat)
        denom = 10**len(str(non_repeat_numer))
        middle = non_repeat_numer

    elif non_repeat != '':
        non_repeat_numer = int(non_repeat)
        repeat_numer = int(repeat_numer)
        denom = int('9'*len(str(repeat_numer))) * 10**len(str(non_repeat_numer))
        middle = non_repeat_numer * int('9'*len(str(repeat_numer)))
    
    else:
        repeat_numer = int(repeat_numer)
        denom = int('9'*len(str(repeat_numer)))
        middle = 0
    
    numer = int_part * denom +\
            middle + repeat_numer

    e = euclid(numer, denom)
    print(n[:-1], '=', numer//e, '/', denom//e)

def euclid(a, b):
    if b > a:
        a, b = b, a
    while True:
        c = a % b
        if c == 0: return b
        a, b = b, c

# while True:
#     try:
#         n = input()
#         test(n)
#     except:
#         break

n = input()
test(n)
