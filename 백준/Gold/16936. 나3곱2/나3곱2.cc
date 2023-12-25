#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <math.h>

using namespace std;

bool compare(const tuple<int, int, long long>& a, const tuple<int, int, long long>& b) {
    if (get<0>(a) == get<0>(b))
        return get<1>(a) < get<1>(b);
    return get<0>(a) > get<0>(b);
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    int N;
    cin >> N;

    vector<tuple<int, int, long long>> arr;
    long long input;
    for (int i = 0; i < N; i++) {
        cin >> input;
        int cnt_2 = 0;
        int cnt_3 = 0;
        long long tmp = input;
        while (tmp % 3 == 0 || tmp % 2 == 0) {
            if (tmp % 3 == 0) {
                cnt_3++;
                tmp /= 3;
            }
            if (tmp % 2 == 0) {
                cnt_2++;
                tmp /= 2;
            }
        }
        arr.push_back(make_tuple(cnt_3, cnt_2, input));
    }

    sort(arr.begin(), arr.end(), compare);

    for (tuple<int, int, long long> p: arr) {
        cout << get<2>(p) << ' ';
    }
}