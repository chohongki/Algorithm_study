#include <iostream>
#include <vector>

using namespace std;

int dp[5000][5000];
int* arr;
int N;

int search(int l, int r) {
    if (l >= r) return 0;

    int& res = dp[l][r];    // res에 저장되는 값은 dp로 바로 저장됨
    if (res != -1) return res;

    if (arr[l] == arr[r]) {
        res = search(l + 1, r - 1);
    }
    else {
        int lres = 1 + search(l + 1, r);
        int rres = 1 + search(l, r - 1);
        res = (lres < rres) ? lres : rres;
    }
    
    return res;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(0);

    cin >> N;

    arr = new int[N];

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    int i = 0;
    int j = N - 1;
    
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			dp[i][j] = -1;
        }
    }
    cout << search(0, N-1);
}