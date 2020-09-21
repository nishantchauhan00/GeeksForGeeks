#include <iostream>
#include <vector>
#include <queue>
#include <stdlib.h>
#include "../utils/BinaryTree.hpp"

using namespace std;

class Solution
{
public:
    vector<int> leftview(TreeNode *root)
    {
        queue<TreeNode *> nodes;
        nodes.push(root);
        vector<int> out;
        while (!nodes.empty())
        {
            int n = nodes.size();
            out.push_back(nodes.front()->val);
            for (int i = 0; i < n; i++)
            {
                root = nodes.front();
                if (root->left)
                    nodes.push(root->left);
                if (root->right)
                    nodes.push(root->right);
                nodes.pop();
            }
        }
        return out;
    }
};

int main(int argc, char const *argv[])
{
    TreeNode *head;
    BinaryTree bt;
    Solution s;

    // int arr[] = {1, 2, 3, 4, 5, 6, 7};
    // head = bt.createBinaryTree(arr, head, 0, 7);
    // int arr[] = {1, 2, 3, 0, 4, 0, 0, 0, 0, 0, 5};
    // head = bt.createBinaryTree(arr, head, 0,11);
    int arr[] = {4, 5, 2, 0, 0, 3, 1, 0, 0, 0, 0, 6, 7};
    head = bt.createBinaryTree(arr, head, 0, 13);

    vector<int> out = s.leftview(head);
    for (int x : out)
        cout << x << " ";

    return 0;
}
