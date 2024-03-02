#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>

class Node
{
    int num;
    std::vector<std::pair<int, int>> child;
    bool visited = false;

public:
    Node() {}
    Node(int n)
    {
        this->num = n;
    }

    void addChild(int n, int d)
    {
        this->child.push_back(std::make_pair(n, d));
    }

    void printAll() 
    {
        for(auto a : this->child) {
            std::cout << a.first << ' ' << a.second << ' ';
        }
        std::cout << std::endl;
    }

    void check_visit()
    {
        this->visited = true;
    }

    void uncheck_visit()
    {
        this->visited = false;
    }

    bool isVisited()
    {
        return this->visited;
    }

    std::vector<std::pair<int, int>> get_childs()
    {
        return this->child;
    }
};

using namespace std;

vector<Node> tree;
int total_length = 0;

int DFS(int n) {
    int first_mxm = 0;
    int second_mxm = 0;

    for(auto a : tree[n].get_childs())
    {
        if (!tree[a.first].isVisited()) 
        {
            tree[a.first].check_visit();

            int mxm = DFS(a.first) + a.second;

            if (first_mxm < mxm)
            {
                second_mxm = first_mxm;
                first_mxm = mxm;
            }
            else if (second_mxm < mxm)
            {
                second_mxm = mxm;
            }
        }
    }

    if (total_length < first_mxm + second_mxm)
    {
        total_length = first_mxm + second_mxm;
    }

    return first_mxm;
}

int main()
{
    ios::sync_with_stdio(false); cin.tie(0);

    int V;

    cin >> V;

    for (int i = 0; i <= V; i++)
    {
        tree.push_back(Node());
    }

    for (int i = 0; i < V; i++)
    {
        int num;
        cin >> num;

        Node a = Node(num);
        while (true)
        {
            int tmp;
            cin >> tmp;

            if (tmp == -1) break;

            int dist;
            cin >> dist;

            a.addChild(tmp, dist);
        }

       tree[num] = a;
    }

    tree[1].check_visit();
    DFS(1);

    std::cout << total_length;

    return 0;
}