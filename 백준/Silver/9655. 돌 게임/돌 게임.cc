#include <iostream>

int main() {
    int N;

    std::cin >> N;

    int dp[1000];
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 2;
    
    
    for(int i = 3; i <= N; i++) {
        dp[i] = std::min(dp[i-1] + 1, dp[i-3] + 1);
    }

    if (dp[N]%2 == 1) std::cout << "SK";
    else std::cout << "CY";

    return 0;
}