#include <iostream>
#include <stack>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    int N;
    cin >> N;

    stack<int> s;
    queue<char> result;
    bool flag = true;
    int before = 0;
    for (int i = 1; i <= N; i++) {
        int tmp;
        cin >> tmp;

        if (tmp > before) {
            for (int j = before+1; j <= tmp; j++) {
                s.push(j);
                result.push('+');
            }
            s.pop();
            result.push('-');

            before = tmp;
        }

        else if (tmp < before) {
            if (tmp == s.top()) {
                result.push('-');
                s.pop();
            }

            else {
                cout << "NO";
                return 0;
            }
        }

        if (before == N && i != N) {
            while(!s.empty()) {
                cin >> tmp;
                if (tmp == s.top()) {
                    result.push('-');
                    s.pop();
                }
                else {
                    cout << "NO";
                    return 0;
                }
                i++;
            }
        }
    }

    while (!result.empty()) {
        cout << result.front() << "\n";
        result.pop();
    }

    return 0;
}