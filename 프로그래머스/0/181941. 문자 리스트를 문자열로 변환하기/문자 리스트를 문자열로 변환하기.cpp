#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(vector<string> arr) {
    string answer = "";
    for (auto c : arr) {
        answer += c;
    }
    return answer;
}