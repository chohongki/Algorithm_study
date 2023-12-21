#include <iostream>
#include <queue>

using namespace std;

int main() {
    int N, M;

    cin >> N >> M;

    int map[N][M] = {0,};

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            char c = cin.get();
            while (c == '\n') c = cin.get();
            map[i][j] = int(c) - int('0');
        }
    }

    int dx[] = {1, 0, -1, 0};
    int dy[] = {0, -1, 0, 1};

    queue<pair<int, int>> q;
    q.push(make_pair(0, 0));
    while (!q.empty()) {
        int now_x = q.front().first;
        int now_y = q.front().second;
        q.pop();

        if (now_x == M-1 && now_y == N-1) {
            cout << map[now_y][now_x];
            break;
        }

        if (map[now_y][now_x] == 0) continue;

        for (int i = 0; i < 4; i++) {
            int nx = now_x + dx[i];
            int ny = now_y + dy[i];

            if (nx < 0 || nx >= M || ny < 0 || ny >= N || map[ny][nx] != 1) continue;

            
            map[ny][nx] = map[now_y][now_x] + 1;
            q.push(make_pair(nx, ny));
        }
    }
    return 0;
}