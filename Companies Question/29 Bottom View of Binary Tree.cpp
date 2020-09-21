#include <iostream>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <map>
#include "../utils/BinaryTree.hpp"

using namespace std;

vector<int> bottomView(TreeNode *root)
{
    vector<int> out;

    if (root == NULL)
        return out;

    int hd = 0;
    map<int, int> m;
    queue<TreeNode *> q;
    queue<int> hdqueue;
    q.push(root);
    hdqueue.push(hd);

    while (!q.empty())
    {
        TreeNode *temp = q.front();
        hd = hdqueue.front();
        q.pop();
        hdqueue.pop();

        m[hd] = temp->val;
        if (temp->left != NULL)
        {
            hdqueue.push(hd - 1);
            q.push(temp->left);
        }
        if (temp->right != NULL)
        {
            hdqueue.push(hd + 1);
            q.push(temp->right);
        }
    }

    for (auto i = m.begin(); i != m.end(); ++i)
        out.push_back(i->second);

    return out;
}

int main(int argc, char const *argv[])
{
    BinaryTree bt;
    TreeNode *root;

    int arr[] = {20, 8, 22, 5, 3, 0, 25, 0, 0, 10, 14};
    root = bt.createBinaryTree(arr, root, 0, 11);
    // // 5 10 3 14 25

    // int arr[] = {20, 8, 22, 5, 3, 4, 25, 0, 0, 10, 0, 14, 0, 14};
    // root = bt.createBinaryTree(arr, root, 0, 14);
    // // 5 10 4 14 25

    vector<int> viewarr;
    viewarr = bottomView(root);

    for (int x : viewarr)
        cout << x << " ";

    return 0;
}
