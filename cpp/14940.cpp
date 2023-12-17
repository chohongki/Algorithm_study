#include <iostream>
#include <queue>

using namespace std;

int n, m;

const int dy[] = {-1, 0, 1, 0};
const int dx[] = {0, 1, 0, -1};

queue<pair<int, int>> q;
int map[1000][1000] = {0,};
int visited[1000][1000] = {0,};
int dst_x, dst_y;

void BFS(int x, int y) {
    q.push({x, y});

    while(q.size()) {
        int now_x = q.front().first;
        int now_y = q.front().second;
        q.pop();    // FIFO므로 bfs 구조

        for (int i = 0; i < 4; i++) {
            int nx = now_x + dx[i];
            int ny = now_y + dy[i];

            // 이미 방문시 스킵
            if (nx < 0 || ny < 0 || nx >= n || ny >= m || map[nx][ny] == 0 || visited[nx][ny]) continue;

            q.push({nx, ny});
            visited[nx][ny] = visited[now_x][now_y] + 1;
        }
    }
}

int main() {
    // 입력
    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> map[i][j];
            if(map[i][j]==2) {
                dst_x = i;
                dst_y = j;
            }
        }
    }

    BFS(dst_x, dst_y);

    // 후처리, 출력
    visited[dst_x][dst_y] = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(visited[i][j]==0 && map[i][j]==1)
                visited[i][j] = -1;
            cout << visited[i][j] << ' ';
        }
        cout << '\n';
    }
}