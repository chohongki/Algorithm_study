#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    ios::sync_with_stdio(0); cin.tie(0);

    int N;
    
    cin >> N;

    int A[50];
    int B[50];

    int tmp;
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    for (int i = 0; i < N; i++) {
        cin >> B[i];
    }

    sort(A, A+N, greater<>());
    sort(B, B+N);

    int sum = 0;
    for (int i = 0; i < N; i++) {
        sum += A[i] * B[i];
    }

    cout << sum;


    return 0;
}