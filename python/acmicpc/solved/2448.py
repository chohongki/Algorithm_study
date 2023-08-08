def makeStar(c):
    global N
    if c >= N-2: return

    for i in range(c):
        for j in range(-c, c):
            arr[c+i][N-c+j] = arr[i][N+j]
            arr[c+i][N+c+j] = arr[i][N+j]

    makeStar(c*2)
    
N = int(input())

arr = [[' '  for _ in range(2*N+1)] for _ in range(N)]

for i in range(3):
    for j in range(-i, i+1):
        arr[i][N+j] = '*'
    arr[1][N] = ' '

if N > 3:
    makeStar(3)

for i in range(N):
    print(''.join(arr[i][1:]))
    