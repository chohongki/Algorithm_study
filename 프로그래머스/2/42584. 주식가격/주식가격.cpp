#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    answer.resize(prices.size());
    
    for (int i = 0; i < prices.size() - 1; i++) {
        bool flag = false;
        int j;
        for (j = i + 1; j < prices.size(); j++) {
            if (prices[i] > prices[j]) {
                answer[i] = j - i;
                flag = true;
                break;
            }
        }
        if (!flag) {
            answer[i] = j - i - 1;
        }
    }
    
    return answer;
}