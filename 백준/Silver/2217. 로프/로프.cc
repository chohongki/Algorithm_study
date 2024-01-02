#include <iostream>
#include <algorithm>

int arr[100000];

using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    int N, tmp;
    int mxm = 0;

    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    sort(arr, arr + N);

    for (int i = N-1; i >= 0; i--) {
        tmp = arr[i] * (N - i);
        if (tmp > mxm) mxm = tmp;
    }

    cout << mxm;

    return 0;
}