#include <iostream>

using namespace std;

int N, M;

int main() {
    cin >> N >> M;

    int map[N][M] = {0,};
    for(int y = 0; y < N; y++) {
        for(int x = 0; x < M; x++) {
            char ch = cin.get();
            if (ch == '\n') ch = cin.get();
            map[y][x] = int(ch) - int('0');
        }
    }

    int mxm = 1;
    int now_sum = 0;

    int mxm_sqr_len = (M < N) ? M : N;
    
    for(int y = 0; y < N-1; y++) {
        for(int x = 0; x < M-1; x++) {
            int now_point = map[y][x];
            for(int len = 1; len <= mxm_sqr_len; len++) {
                if (x+len >= M || y+len >= N) continue;
                if (now_point == map[y+len][x] &&
                    now_point == map[y][x+len] &&
                    now_point == map[y+len][x+len]) {

                    now_sum = (len + 1) * (len + 1);
                    if (mxm < now_sum) mxm = now_sum;
                }
            }
        }
    }
    
    cout << mxm;
    return 0;
}