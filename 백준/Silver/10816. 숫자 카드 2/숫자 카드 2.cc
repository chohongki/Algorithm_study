#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    unordered_map<int, int> map1;
    int N, M, tmp;

    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> tmp;
        if (map1.find(tmp) != map1.end()) {
            map1[tmp]++;
        }
        else {
            map1.insert(make_pair(tmp, 1));
        }
    }
    
    cin >> M;

    for (int i = 0; i < M; i++) {
        cin >> tmp;
        if (map1.find(tmp) != map1.end()) {
            cout << map1[tmp] << ' ';
        }
        else {
            cout << 0 << ' ';
        }
    }
}