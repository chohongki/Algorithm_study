#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
struct Compare {
    bool operator()(vector<int>& a, vector<int>& b) {
        if (a[0] == b[0]) {
            if (a[1] == b[1]) return a[2] > b[2];
            return a[1] > b[1];
        }
        return a[0] > b[0];
    }
};

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    vector<vector<int>> sorted_jobs;    // 시작, 실행시간, idx
    
    for (int i = 0; i < jobs.size(); i++) {
        sorted_jobs.push_back({jobs[i][0], jobs[i][1], i});
    }
    
    sort(sorted_jobs.begin(), sorted_jobs.end(), [](const vector<int>& a, const vector<int>& b){
        return a[0] < b[0];
    });
    
    vector<int> current_job;
    int current_time = 0;
    int idx = 0;
    int done = 0;
    priority_queue<vector<int>, vector<vector<int>>, Compare> pq;    // 실행시간, 시작, idx
    while (done < jobs.size()) {     
        // 현재 시간보다 이전 작업들 전부 넣기
        while (idx < jobs.size() && current_time >= sorted_jobs[idx][0]) {
            pq.push({sorted_jobs[idx][1], sorted_jobs[idx][0], sorted_jobs[idx][2]});
            idx++;
        }
        
        if (pq.empty()) current_time = sorted_jobs[idx][0];
        else {
            current_job = pq.top();
            pq.pop();
            current_time += current_job[0];
            answer += current_time - current_job[1];
            done++;
        }
        
    }
    
    return answer / jobs.size();
}