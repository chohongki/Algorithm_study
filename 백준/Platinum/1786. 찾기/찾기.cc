#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    string T;
    string P;

    getline(cin, T);
    getline(cin, P);


    int cnt = 0;
    int i, j;

    vector<int> table;
    vector<int> idx_list;


    table.resize(P.size(), 0);

    j = 0;
    for (i = 1; i < P.size(); i++) {
        while (j > 0 && P[i] != P[j]) {
            j = table[j-1];
        }
        if (P[i] == P[j]) {
            table[i] = ++j;
        }
    }

    j = 0;
    for (i = 0; i < T.size(); i++) {

        while (j > 0 && T[i] != P[j]){
            j = table[j-1];
        }
        if (T[i] == P[j]) {
            if (j == P.size() - 1) {
                idx_list.push_back(i - P.size() + 2);
                cnt++;
                j = table[j];
            }
            else {
                j++;
            }
        }
    }

    cout << cnt << "\n";
    for(auto &i : idx_list) {
        cout << i << " ";
    }

    return 0;
}