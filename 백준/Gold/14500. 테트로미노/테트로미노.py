import sys

input = sys.stdin.readline

N, M = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

def search(x, y):
    tmp = [-1]
    tmp.append(typeI(x, y))
    tmp.append(typeO(x, y))
    tmp.append(typeL(x, y))
    tmp.append(typeZ(x, y))
    tmp.append(typeT(x, y))

    return max(tmp)

def typeI(x, y):
    tmp = [-1]
    if y+3 < N:
        tmp.append(grid[y][x]+grid[y+1][x]+grid[y+2][x]+grid[y+3][x])
    if x+3 < M:
        tmp.append(grid[y][x]+grid[y][x+1]+grid[y][x+2]+grid[y][x+3])    
    return max(tmp)

def typeO(x, y):
    if x+1 < M and y+1 < N:
        return grid[y][x]+grid[y][x+1]+grid[y+1][x]+grid[y+1][x+1]
    else:
        return -1

def typeL(x, y):
    tmp = [-1]
    if y+2 < N and x+1 < M:
        tmp.append(grid[y][x]+grid[y+1][x]+grid[y+2][x]+grid[y+2][x+1])
        tmp.append(grid[y][x]+grid[y+1][x]+grid[y+2][x]+grid[y][x+1])
        tmp.append(grid[y][x]+grid[y][x+1]+grid[y+1][x+1]+grid[y+2][x+1])
        tmp.append(grid[y+2][x]+grid[y][x+1]+grid[y+1][x+1]+grid[y+2][x+1])
        
    if x+2 < M and y+1 < N:
        tmp.append(grid[y][x]+grid[y][x+1]+grid[y][x+2]+grid[y+1][x+2])
        tmp.append(grid[y][x]+grid[y][x+1]+grid[y][x+2]+grid[y+1][x])
        tmp.append(grid[y+1][x]+grid[y+1][x+1]+grid[y+1][x+2]+grid[y][x+2])
        tmp.append(grid[y+1][x]+grid[y+1][x+1]+grid[y+1][x+2]+grid[y][x])

    return max(tmp)

def typeZ(x, y):
    tmp = [-1]
    if y+2 < N and x+1 < M:
        tmp.append(grid[y][x]+grid[y+1][x]+grid[y+1][x+1]+grid[y+2][x+1])
        tmp.append(grid[y][x+1]+grid[y+1][x+1]+grid[y+1][x]+grid[y+2][x])
        
    if x+2 < M and y+1 < N:
        tmp.append(grid[y][x]+grid[y][x+1]+grid[y+1][x+1]+grid[y+1][x+2])
        tmp.append(grid[y+1][x]+grid[y+1][x+1]+grid[y][x+1]+grid[y][x+2])
    
    return max(tmp)

def typeT(x, y):
    tmp = [-1]
    if y+2 < N and x+1 < M:
        tmp.append(grid[y][x]+grid[y+1][x]+grid[y+2][x]+grid[y+1][x+1])
        tmp.append(grid[y][x+1]+grid[y+1][x+1]+grid[y+2][x+1]+grid[y+1][x])
        
    if x+2 < M and y+1 < N:
        tmp.append(grid[y][x]+grid[y][x+1]+grid[y][x+2]+grid[y+1][x+1])
        tmp.append(grid[y+1][x]+grid[y+1][x+1]+grid[y+1][x+2]+grid[y][x+1])
    
    return max(tmp)


mxm = 0
for y in range(N):
    for x in range(M):
        v = search(x, y)
        if v > mxm:
            mxm = v

print(mxm)