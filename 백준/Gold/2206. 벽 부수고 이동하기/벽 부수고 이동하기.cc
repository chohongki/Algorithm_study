#include <iostream>
#include <vector>
#include <tuple>
#include <queue>

using namespace std;

typedef struct {
    int x;
    int y;
    int distance;
    int brk;
}node;


int map[1001][1001] = {0,};
bool visited[1001][1001][2] = {0,};

int main() {
    int N, M;
    cin >> N >> M;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            scanf("%1d", &map[i][j]);
        }
    }

    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, -1, 0, 1};

    queue<node> q;   // x, y, distance, 벽 부순 여부
    q.push({0, 0, 1, 0});

    int max_distance = 1001 * 1001 + 1;
    
    node now;
    while (!q.empty()) {
        now = q.front();
        q.pop();

        // if (visited[now.y][now.x] && now.brk) {continue;}

        if (now.x == M-1 && now.y == N-1) {
            if (max_distance > now.distance) {max_distance = now.distance;}
            continue;
        }

        for(int i = 0; i < 4; i++) {
            int nx = now.x + dx[i];
            int ny = now.y + dy[i];


            if (nx < 0 || nx > M-1 || ny < 0 || ny > N-1) {continue;}
            if (visited[ny][nx][now.brk]) {continue;}
            
            // cout << now.x << ',' << now.y << ','<< now.distance << ',' << now.brk << '\n';

            if (now.brk) {
                if (map[ny][nx] == 1) {continue;}
                else {
                    visited[ny][nx][now.brk] = true;
                    q.push({nx, ny, now.distance + 1, true});
                }
            }
            else {
                visited[ny][nx][(now.brk || map[ny][nx])] = true;
                q.push({nx, ny, now.distance + 1, (now.brk || map[ny][nx])});
            }
            
        }

    }

    if (max_distance < N * M + 1) {cout << max_distance;}
    else {cout << -1;}

    return 0;
}