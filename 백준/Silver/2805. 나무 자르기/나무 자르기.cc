#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

    int N, M;

    cin >> N >> M;

    int tmp;
    vector<int> arr;
    for (int i = 0; i < N; i++) {
        cin >> tmp;
        arr.push_back(tmp);
    }
    
    sort(arr.begin(), arr.end());

    int forward, middle, backward;
    forward = 0; backward = arr[N-1];

    int res = 0;
    long long sum = 0;
    while (forward <= backward) {
        middle = (backward + forward) / 2;
        
        sum = 0;
        for (int i = 0; i < N; i++) {
            if (arr[i] - middle > 0) sum += arr[i] - middle;
        }

        if (sum >= M) {
            res = middle;
            forward = middle + 1;
        }
        else {
            backward = middle - 1;
        }

    }

    cout << res;

    return 0;
}