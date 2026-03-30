#include <iostream>

using namespace std;

int main() {
    int A, P, C;
    cin >> A >> P >> C;
    
    int result = (A+C > P) ? A+C : P;
    cout << result;

    return 0;
}