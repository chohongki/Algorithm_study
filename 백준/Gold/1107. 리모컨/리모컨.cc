#include <iostream>
#include <queue>
#include <string>

using namespace std;

#define f_MIN(a, b) (a < b ? a : b)

int min_cnt = 500000;
int unable[10];
int target;

int length(int n)
{
    if (n == 0) return 0;
    int cnt = 1;
    while (n >= 10)
    {
        n /= 10;
        cnt ++;
    }

    return cnt;
}

void find(int n)
{
    int tmp_len = length(n);

    if (tmp_len > min_cnt || n > 500000) return;

    for (int i = 0; i < 10; i++)
    {
        if (!unable[i])
        {
            int tmp = n * 10 + i;        
            int tmp_cnt = tmp_len + 1 + abs(target - tmp);

            if (min_cnt > tmp_cnt) min_cnt = tmp_cnt;

            if (tmp) find(tmp);
        }
    }

}

int main() 
{
    ios::sync_with_stdio(false);cin.tie(0);
    
    int M;

    cin >> target;
    cin >> M;

    min_cnt = abs(100 - target);

    if (M == 0 && target != 0) min_cnt = f_MIN(min_cnt, length(target));

    else 
    {
        for (int i = 0; i < M; i++) 
        {
            int tmp;
            cin >> tmp;

            unable[tmp] = 1;
        }

        min_cnt = f_MIN(min_cnt, abs(100 - target));

        find(0);
    }
    cout << min_cnt;

    return 0;
}