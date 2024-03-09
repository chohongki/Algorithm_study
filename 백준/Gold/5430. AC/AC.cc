#include <iostream>
#include <deque>
#include <string>

using namespace std;

void print(deque<int> &arr)
{
    cout << "[";
    for (int i = 0; i < arr.size(); i++)
    {
        cout << arr[i];
        if (i != arr.size() - 1) cout << ",";
    }
    cout << "]\n";
}

void reverse_print(deque<int> &arr)
{
    cout << "[";
    if (arr.size() != 0) 
    for (int i = arr.size() - 1; i >= 0; i--)
    {
        cout << arr[i];
        if (i != 0) cout << ",";
    }
    cout << "]\n";
}

void test()
{
    string p;
    int n;
    string tmp_input;
    deque<int> arr;
    bool is_reversed = false;

    cin >> p;
    cin >> n;
    cin >> tmp_input;

    string tmp = "";
    for (int i = 0; i < tmp_input.size(); i++)
    {
        if (tmp_input[i] == '[') continue;

        else if (tmp_input[i] == ']' || tmp_input[i] == ',') 
        {
            if (tmp.length() != 0) arr.push_back(stoi(tmp));
            tmp = "";
            continue;
        }
        
        else tmp += tmp_input[i];
    }

    for (int i = 0; i < p.size(); i++)
    {
        if (p[i] == 'R') is_reversed = !is_reversed;
        else if (p[i] == 'D')
        {
            if (arr.size() == 0)
            {
                cout << "error\n";
                return;
            }
            if (is_reversed) arr.pop_back();
            else arr.pop_front();
        }
    }

    if (is_reversed) reverse_print(arr);
    else print(arr);
}

int main()
{
    int T;

    cin >> T;

    for (int i = 0; i < T; i++) test();
    
    return 0;
}