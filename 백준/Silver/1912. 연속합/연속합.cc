#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    int n;

    cin >> n;

    int seq[n] = {0,};
    int dp[n] = {0,};
    for (int i = 0; i < n; i++) {
        cin >> seq[i];
    }
    
    int mxm = seq[0];
    dp[0] = seq[0];
    for (int i = 1; i < n; i++) {
        dp[i] = (dp[i-1] + seq[i] > seq[i]) ? dp[i-1] + seq[i] : seq[i];
        mxm = (dp[i] > mxm) ? dp[i] : mxm;
    }

    cout << mxm;

    return 0;
}