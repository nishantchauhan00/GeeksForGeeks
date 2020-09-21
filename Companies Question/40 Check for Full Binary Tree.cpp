/*
full binary tree have all nodes full 
*/

#include <iostream>
#include <stdlib.h>
#include <vector>
#include "../utils/BinaryTree.hpp"

using namespace std;

bool isFullBinaryTree(TreeNode *root)
{
    if (!root)
        return true;

    int n = 1;
    queue<TreeNode *> nodequeue;
    nodequeue.push(root);

    while (!nodequeue.empty())
    {
        if (nodequeue.size() != n)
            return false;

        for (int i = 0; i < n; i++)
        {
            TreeNode *nnode = nodequeue.front();
            nodequeue.pop();
            if (nnode->left)
                nodequeue.push(nnode->left);
            if (nnode->right)
                nodequeue.push(nnode->right);
        }
        n = 2*n;
    }

    return true;
}

int main(int argc, char const *argv[])
{
    TreeNode *head;
    BinaryTree bt;

    int arr[] = {15, 7, 16, 1, 12, 0, 0, 0, 2, 10, 14};
    head = bt.createBinaryTree(arr, head, 0, 11);

    cout << isFullBinaryTree(head);

    return 0;
}
