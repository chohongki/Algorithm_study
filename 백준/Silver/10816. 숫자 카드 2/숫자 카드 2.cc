#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M, a, b;

	vector<int> v;

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> a;
		v.push_back(a);
	}

	sort(v.begin(), v.end());
	
    cin >> M;
	for (int i = 0; i < M; i++) {
		cin >> b;
		auto lower = lower_bound(v.begin(), v.end(), b);
		auto upper = upper_bound(v.begin(), v.end(), b);
		cout << upper - lower << " ";
	}
	return 0;
}