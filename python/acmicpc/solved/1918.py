def priority(s):
    if s=='+' or s=='-': return 1
    if s=='*' or s=='/': return 2
    return 0

infix = list(input())


stack = []
res = ""

for i in range(len(infix)):
    c = infix[i]
    if c >='A' and c <='Z':
        res += c
        continue
    if not stack or c=="(":
        stack.append(c)
        continue
    if c==')':
        while stack[-1]!="(":
            res += stack.pop()
        stack.pop()
        continue
    if priority(stack[-1]) < priority(c):
        stack.append(c)
    else:
        while stack and priority(stack[-1]) >= priority(c):
            res += stack.pop()
        stack.append(c)


while stack:
    res += stack.pop()

print(res)

