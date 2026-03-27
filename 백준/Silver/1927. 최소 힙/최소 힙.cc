#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int N;
    cin >> N;

    priority_queue<uint32_t, vector<uint32_t>, greater<uint32_t>> q;

    for (int i = 0; i < N; i++) {
        uint32_t x;
        cin >> x;

        if (x == 0) {
            if (q.empty()) {
                cout << 0 << '\n';
                continue;
            }
            cout << q.top() << '\n';
            q.pop();
        }
        else {
            q.emplace(x);
        }
    }

    return 0;
}