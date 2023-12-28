#include <iostream>
#include <math.h>

using namespace std;

long long arr[101] = {0,};

long long P(int i) {
    if (i == 1 || i == 2 || i == 3) return 1;
    if (i == 4 || i == 5) return 2;
    if(i == 6) return 3;

    if (arr[i] == 0) arr[i] = P(i-1) + P(i-5);

    return arr[i];
}

void test() {
    int N;
    cin >> N;
    cout << P(N) << '\n';
}

int main() {
    int T;

    cin >> T;

    for (int i = 0; i < T; i++) {
        test();
    }

    return 0;
}