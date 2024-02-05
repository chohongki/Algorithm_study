#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    int N, M;

    cin >> N >> M;

    vector<int>* arr = new vector<int>[N+1];
    int* cnt = new int[N+1]{0};

    for (int i = 0; i < M; i++) {
        int a, b;

        cin >> a >> b;
        
        cnt[b]++;
        arr[a].push_back(b);
    }

    queue<int> q;
    for (int i = 1; i <= N; i++) {
        if (cnt[i] == 0) q.push(i);
    }

    while (!q.empty()) {
        int current = q.front();
        q.pop();

        cout << current << ' ';

        for(int i = 0; i < arr[current].size(); i++) {
            int next = arr[current][i];
            cnt[next]--;

            if (cnt[next] == 0) q.push(next);
        }
    }

    return 0;
}