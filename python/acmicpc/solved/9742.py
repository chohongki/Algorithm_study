import sys

def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def test(word, i):
    print(word + " " + str(i) + " = ", end = "")
    s = ""
    L = len(word)
    if i > factorial(L):
        print("No permutation")
        return

    else :
        word = list(word)
        i -= 1
        for j in range(L-1, 0, -1):
            t = factorial(j)
            s += word.pop(i//t)
            i %= t
        print(s + word.pop())
        return
        

def __init__():
    while True:
        try:
            word, i = sys.stdin.readline().split()
        except:
            break
        test(word, int(i))

__init__()