#include <iostream>
#include <deque>

using namespace std;

int main() {
    int N;
    cin >> N;

    deque<int> q;

    for (int i = 1; i <= N; i++) {
        q.emplace_back(i);
    }

    while (q.size() > 1) {
        q.pop_front();
        q.emplace_back(q[0]);
        q.pop_front();
    }

    cout << q[0];

    return 0;
}