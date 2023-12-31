#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, tmp;
    int cnt = 0;

    cin >> N;
    
    int arr[N+1] = {0,};

    for (int i = 1; i <= N; i++) {
        cin >> tmp;

        cnt = 0;
        for (int j = 1; j <= N; j++) {
            if (cnt == tmp && arr[j] == 0) {
                arr[j] = i;
                break;
            }
            else if (arr[j] == 0) cnt++;
        }

    }

    for (int i = 1; i <= N; i++) {
        cout << arr[i] << ' ';
    }

    return 0;
}