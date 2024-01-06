#include <iostream>
#include <string>
#include <cstring>

using namespace std;


int main() {
    ios::sync_with_stdio(0); cin.tie(0);

    int S[21] = {0,};
    int M;
    string str;
    int x;

    cin >> M;
    
    for (int i = 1; i <= M; i++) {
        cin >> str;

        if (str == "all") {
            fill(S, S+21, 1);
        }

        else if (str == "empty") {
            memset(S, 0, sizeof(S));
        }

        else {
            cin >> x;

            if (str == "add") {
                S[x] = 1;
            }
            
            else if (str == "check") {
                cout << S[x] << '\n';
            }
            
            else if (str == "toggle") {
                S[x] = !S[x];
            }
            
            else if (str == "remove") {
                S[x] = 0;
            }
        }
    }

    return 0;
}