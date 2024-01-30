#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;


bool cmp(long &a, long &b) {return a > b;}

int main() {
    int N;
    long table[26] = {0,};

    cin >> N;

    char** arr = new char*[N];

    for (int i = 0; i < N; i++) {
        arr[i] = new char[9];

        cin >> arr[i];

        long power = 1;
        for (int j = strlen(arr[i]) - 1; j >= 0; j--) {
            table[arr[i][j] - 65] += power;
            power *= 10;
        }
    }

    sort(table, table+26, cmp);

    long res = 0;
    long mul = 9;
    for (int i = 0; i < 26; i++) {
        if (table[i] == 0) continue;

        res += mul * table[i];
        mul--;
    }

    cout << res;
    
    return 0;
}