#include <iostream>

using namespace std;

char LR[] = {'0', '1' , '5', '?', '?', '2', '?', '?', '8', '?'};
char UD[] = {'0', '1' , '5', '?', '?', '2', '?', '?', '8', '?'};
char W;
int N;
int arr[20][20];

void convertRL() {
    for (int i = 0; i < N; i++) {
        for (int j = N-1; j >= 0; j--) {
            cout << LR[arr[i][j]] << ' ';
        }
        if (i < N-1) cout << '\n';
    }
}

void convertUD() {
    for (int i = N-1; i >= 0 ; i--) {
        for (int j = 0; j < N; j++) {
            cout << UD[arr[i][j]] << ' ';
        }
        if (i > 0) cout << '\n';
    }
}

int main() {
    cin >> W >> N;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> arr[i][j];
        }
    }

    switch (W) {
        case 'L':
        case 'R':
            convertRL();
            break;
        case 'U':
        case 'D':
            convertUD();
            break;
    }
    

    return 0;
}