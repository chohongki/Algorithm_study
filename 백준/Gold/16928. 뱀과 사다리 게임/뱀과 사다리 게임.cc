#include <iostream>
#include <queue>

using namespace std;

int main()
{
    int N, M;

    cin >> N >> M;
    
    int ladder[101] = {0,};
    int visited[101] = {0,};

    for (int i = 0; i < N; i++) {
        int x, y;
        cin >> x >> y;
        ladder[x] = y; 
    }
    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v; 
        ladder[u] = v;   
    }

    int pos = 1;
    queue<pair<int, int>> q;

    q.push(make_pair(1, 0));

    while(!q.empty()) {
        int now_pos = q.front().first;
        int now_depth = q.front().second;
        q.pop();

        visited[now_pos] = 1;

        if (now_pos == 100) {
            cout << now_depth << endl;
            break;
        }

        for (int i = 1; i <= 6; i++) {
            int next = now_pos + i;
            if (next > 100 || visited[next]) continue;
            if (ladder[next] != 0) {
                next = ladder[next];
            }
            q.push(make_pair(next, now_depth + 1));
        }
    }

    return 0;
}