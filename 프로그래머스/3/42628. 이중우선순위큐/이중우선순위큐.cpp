#include <string>
#include <vector>
#include <set>

using namespace std;

vector<int> solution(vector<string> arguments) {
    vector<int> answer;
    multiset<int> ms;
    multiset<int>::iterator iter;

    for(auto s : arguments) {
        if (s[0] == 'I') ms.insert(stoi(s.substr(2))); 
        else if (ms.size() > 0) {
            if (s.substr(2,1) == "1") ms.erase(--ms.end());
            else ms.erase(ms.begin());
        }
    }

    if(ms.size() == 0) return {0, 0};

    return {*ms.rbegin(), *ms.begin()};
}
