#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    int w = 0;
    int h = 0;
    
    for (auto s : sizes) {
        w = max(w, max(s[0], s[1]));
        h = max(h, min(s[0], s[1]));
    }
    
    return w * h;
}