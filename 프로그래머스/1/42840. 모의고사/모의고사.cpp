#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> correct(3);
    
    const vector<vector<int>> supos = {{1, 2, 3, 4, 5}, {2, 1, 2, 3, 2, 4, 2, 5}, {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}};
    
    for (int i = 0; i < answers.size(); i++) {
        for (int j = 0; j < 3; j++) {
            if (answers[i] == supos[j][i % supos[j].size()]) correct[j]++;
        }
    }
    
    int mxm = *max_element(correct.begin(), correct.end());
    for (int i = 0; i < 3; i++) {
        if (correct[i] == mxm) answer.emplace_back(i+1);
    }
    
    return answer;
}