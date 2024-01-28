#include <iostream>
#include <algorithm>
#include <tuple>

using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(0);

    int N;

    cin >> N;

    int* arr = new int[N];

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    sort(arr, arr + N);

    int start = 0;
    int end = N-1;
    int now = abs(arr[start] + arr[end]);

    tuple<int, int, int> res = make_tuple(start, end, now);

    while (start < end) {
        now = arr[start] + arr[end];

        if (now == 0) {
            res = make_tuple(start, end, now);
            break;
        }

        else if (now < 0) {
            if (abs(now) < abs(get<2>(res))){
                res = make_tuple(start, end, now);
            }
            else if (arr[start] > 0) break;
            start += 1;
        }

        else {
            if (abs(now) < abs(get<2>(res))){
                res = make_tuple(start, end, now);
            }
            else if (arr[end] < 0) break;
            end -= 1;
        }
    }

    cout << arr[get<0>(res)] << ' ' << arr[get<1>(res)];

    return 0;
}