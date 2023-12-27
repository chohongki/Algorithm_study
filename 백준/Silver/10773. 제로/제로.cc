#include <iostream>
#include <stack>

using namespace std;

int main() {
    int K;

    cin >> K;

    int n;
    stack<int> s;
    for (int i = 0; i < K; i++) {
        scanf("%d", &n);
        if (n == 0) {
            s.pop();
        }
        else {
            s.push(n);
        }
    }

    long long sum = 0;
    while (!s.empty()) {
        sum += s.top();
        s.pop();
    }

    cout << sum;

    return 0;
}