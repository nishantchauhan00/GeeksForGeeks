#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

struct TrieNode
{
    TrieNode *next[26];
    bool isEnd;
    TrieNode()
    {
        isEnd = false;
        for (int i = 0; i < 26; i++)
            next[i] = NULL;
    }
};

void insert(TrieNode *root, string inp)
{
    TrieNode *head = root;
    int slen = inp.size();
    for (int i = 0; i < slen; i++)
    {
        int pos = (int)inp[i] - 97;
        if (head->next[pos] == NULL)
        {
            // try direct new node after
            head->next[pos] = new TrieNode();
        }
        head = head->next[pos];
    }
    head->isEnd = true;
}

void getNodes(TrieNode *root, string curr, vector<string> &out)
{
    if (root->isEnd)
        out.push_back(curr);
    for (int i = 0; i < 26; i++)
        if (root->next[i] != NULL)
            getNodes(root->next[i], curr + (char)(i + 97), out);
}

void search(TrieNode *root, string inp)
{
    for (int i = 0; i < inp.size(); i++)
    {
        if (root->next[(int)inp[i] - 97] == NULL)
        {
            cout << "0\n";
            return;
        }
        root = root->next[(int)inp[i] - 97];
    }

    vector<string> out;
    /*
    // using queue
    queue<pair<TrieNode *, string>> qu;
    pair<TrieNode *, string> temp;
    TrieNode *tempnode;
    qu.push(make_pair(root, inp));
    while (!qu.empty())
    {
        temp = qu.front();
        qu.pop();
        if (temp.first->isEnd)
            out.push_back(temp.second);
        for (int i = 0; i < 26; i++)
            if (temp.first->next[i] != NULL)
            {
                tempnode = temp.first;
                qu.push(make_pair(tempnode->next[i], temp.second + (char)(i + 97)));
            }
    }

    sort(out.begin(), out.end());
    */

    // one good thing about recursion is we dont need to sort
    getNodes(root, inp, out);

    for (string el : out)
        cout << el << " ";
    cout << "\n";
}

void solver(int n, string nums[], string inp)
{
    TrieNode *root = new TrieNode();
    for (int i = 0; i < n; i++)
        insert(root, nums[i]);

    for (int i = 0; i < inp.size(); i++)
        search(root, inp.substr(0, i + 1));
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        string nums[n];
        for (int i = 0; i < n; i++)
            cin >> nums[i];
        string inp;
        cin >> inp;

        solver(n, nums, inp);
    }
    return 0;
}