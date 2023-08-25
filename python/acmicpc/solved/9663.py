# 미친풀이 https://rebas.kr/761

def nqueen(y):
    global N, cnt
    
    if y == N: 
        cnt += 1
        return

    for i in range(N):
        if not (ver_mask[i] or diagon_mask[i+y] or anti_diagon_mask[i+(N-y)-1]):
            ver_mask[i] =\
                diagon_mask[i+y] =\
                anti_diagon_mask[i+(N-y)-1] = True
            nqueen(y+1)
            ver_mask[i] =\
                diagon_mask[i+y] =\
                anti_diagon_mask[i+(N-y)-1] = False

if __name__ == '__main__':
    N = int(input())

    # 마스킹으로 수직, 대각 체킹
    ver_mask = [False for _ in range(N)]
    diagon_mask = [False for _ in range(2*N-1)]
    anti_diagon_mask = [False for _ in range(2*N-1)]

    cnt = 0

    # 답이 symmetry 함
    for i in range(N//2):
        ver_mask[i] =\
            diagon_mask[i] =\
            anti_diagon_mask[i+N-1] = True
        nqueen(1)
        ver_mask[i] =\
            diagon_mask[i] =\
            anti_diagon_mask[i+N-1] = False
    cnt *= 2

    if N%2:
        ver_mask[N//2] =\
            diagon_mask[N//2] =\
            anti_diagon_mask[N//2+N-1] = True
        nqueen(1)
        ver_mask[N//2] =\
            diagon_mask[N//2] =\
            anti_diagon_mask[N//2+N-1] = False

    print(cnt)