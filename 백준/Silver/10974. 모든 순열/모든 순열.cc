#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int visited[9];
int N;
vector<int> v;

void func() {
    if (v.size() == N) {
        for (int i = 0; i < N; i++) {
            cout << v[i] << ' ';
        }
        cout << "\n";
    }

    for (int i = 1; i <= N; i++) {
        if (!visited[i]) {
            v.push_back(i);
            visited[i] = 1;
            func();
            v.pop_back();
            visited[i] = 0;
        }
    }
}

int main() {

    cin >> N;

    func();
    
    return 0;
}