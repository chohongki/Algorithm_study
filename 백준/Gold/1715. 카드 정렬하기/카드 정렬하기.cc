#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
    int N;

    cin >> N;  

    if (N == 1) {
        cout << 0;
        return 0;
    }

    int tmp;
    priority_queue<int, vector<int>, greater<int>> cards;
    for (int i = 0; i < N; i++) {
        cin >> tmp;
        cards.push(tmp);
    }
    
    int idx = 0;
    int sum = 0;
    while (cards.size() >= 2) {
        int a = cards.top();
        cards.pop();
        int b = cards.top();
        cards.pop();

        sum += a + b;
        cards.push(a + b);
    }
    
    cout << sum;

    return 0;
}