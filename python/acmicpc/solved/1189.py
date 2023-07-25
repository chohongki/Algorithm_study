R, C, K = map(int, input().split())
graph = [list(input()) for _ in range(R)]
res = 0

def DFS(x, y, i):
    global res
    if (x,y) == (0, C-1) and i == K: 
        res += 1
    else:
        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
            nx, ny = x+dx, y+dy
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != 'T':
                graph[nx][ny]='T'
                DFS(nx,ny,i+1)
                graph[nx][ny]='.'

graph[R-1][0] = 'T'
DFS(R-1, 0 , 1)
print(res)