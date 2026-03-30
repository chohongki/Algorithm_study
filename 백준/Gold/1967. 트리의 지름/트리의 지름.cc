#include <iostream>
#include <vector>

using namespace std;

class Node {
    int num;
    vector<pair<int, int>> childs;
    bool visited;

public:
    Node() {}
    Node(int n) { this->num = n; }

    int getNum() { return this->num; }

    vector<pair<int, int>> getChilds() {
        return this->childs;
    }

    void checkVisited() {
        this->visited = true;
    }

    void uncheckVisited() {
        this->visited = false;
    }

    bool isVisited() {
        return this->visited;
    }

    void addChild(int num, int dist) {
        this->childs.emplace_back(make_pair(num, dist));
    }

    void printAll() 
    {
        for(auto a : this->childs) {
            cout << a.first << ' ' << a.second << ' ';
        }
        cout << '\n';
    }
};

int DFS(int start, int& tot_max, vector<Node>& tree) {
    int first_max = 0;
    int second_max = 0;

    for(auto c : tree[start].getChilds()) {
        if (!tree[c.first].isVisited()) {
            tree[c.first].checkVisited();
            int mxm = DFS(c.first, tot_max, tree) + c.second;

            if (first_max < mxm) {
                second_max = first_max;
                first_max = mxm;  
            }
            else if (second_max < mxm) {
                second_max = mxm;
            }
        }
    }

    if (first_max + second_max > tot_max) {
        tot_max = first_max + second_max;
    }

    return first_max;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int N;
    cin >> N;

    vector<Node> tree;
    tree.resize(N+1);
    // for (int i = 1 ; i < N; i++) {
    //     tree.emplace_back(Node(i));
    // }

    for (int i = 1 ; i < N; i++) {
        int parent, child, dist;
        cin >> parent >> child >> dist;

        tree[parent].addChild(child, dist);        
    }

    int tot_max = 0;

    tree[1].checkVisited();
    DFS(1, tot_max, tree);
    cout << tot_max;

    return 0;
}