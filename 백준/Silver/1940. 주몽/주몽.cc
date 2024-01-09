#include <iostream>

using namespace std;

int main() {
    int N, M;

    cin >> N >> M;

    int arr[15000];
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    int res = 0;
    for (int i = 0; i < N - 1; i++) {
        for (int j = i + 1; j < N; j++) {
            if (arr[i] + arr[j] == M) {
                res++;
            }
        }
    }

    cout << res;

    return 0;
}


