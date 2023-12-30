#include <iostream>
#include <math.h>

using namespace std;


int main() {
    int map[100][100] = {0,};

    int r1, c1, r2, c2;
    int n, d, sum;
    int max_num = 0;

    cin >> r1 >> c1 >> r2 >> c2;

    for (int i = r1; i <= r2; i++) { // y
        for (int j = c1; j <= c2; j++) { // x
            n = max(abs(j), abs(i));
            d = 2 * n + 1;
            sum = d * d; 

            if (i == n) {
                map[i-r1][j-c1] = sum - (n - j); 
            }
            sum -= d - 1;
            if (j == -n) {
                map[i-r1][j-c1] = sum - (n - i); 
            }
            sum -= d - 1;
            if (i == -n) {
                map[i-r1][j-c1] = sum - (n + j); 
            }
            sum -= d - 1;
            if (j == n && i != n) {
                map[i-r1][j-c1] = sum - (n + i); 
            }
            if (map[i-r1][j-c1] > max_num) max_num = map[i-r1][j-c1];
        }
    }

    int max_len = 1;
    while(max_num >= 10) {
        max_num /= 10;
        max_len++;
    }

    for (int i = r1; i <= r2; i++) { // y
        for  (int j = c1; j <= c2; j++) { // x
            printf("%*d ", int(max_len), map[i-r1][j-c1]);
        }
        printf("\n");
    }

    return 0;
}