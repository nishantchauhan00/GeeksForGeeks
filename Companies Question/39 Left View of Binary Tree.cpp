#include <iostream>
#include <stdlib.h>
#include <vector>
#include "../utils/BinaryTree.hpp"

using namespace std;

void leftView(TreeNode *root)
{
    if (!root)
        return;

    vector<int> out;
    int n = 1;
    queue<TreeNode *> nodequeue;
    nodequeue.push(root);

    while (!nodequeue.empty())
    {
        TreeNode *nnode = nodequeue.front();
        out.push_back(nnode->val);

        int count = 0;
        for (int i = 0; i < n; i++)
        {
            TreeNode *nnode = nodequeue.front();
            nodequeue.pop();
            if (nnode->left)
            {
                count++;
                nodequeue.push(nnode->left);
            }
            if (nnode->right)
            {
                count++;
                nodequeue.push(nnode->right);
            }
        }
        n = count;
    }

    for (int x : out)
        printf("%d ", x);
    printf("\n");
}

int main(int argc, char const *argv[])
{
    TreeNode *head;
    BinaryTree bt;

    int arr[] = {1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 8};
    head = bt.createBinaryTree(arr, head, 0, 11);
    // 1 2 4 8

    leftView(head);

    return 0;
}
