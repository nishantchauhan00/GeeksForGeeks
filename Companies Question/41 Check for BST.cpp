/*
full binary tree have all nodes full 
*/

#include <iostream>
#include <stdlib.h>
#include <vector>
#include "../utils/BinaryTree.hpp"

using namespace std;

void inorder(vector<int> &vec, TreeNode *head)
{
    if (!head)
        return;

    inorder(vec, head->left);
    vec.push_back(head->val);
    inorder(vec, head->right);
}

bool isBST(TreeNode *root)
{
    vector<int> vec;
    inorder(vec, root);

    if (vec.size() < 2)
        return true;

    for (int i = 0; i < vec.size() - 1; i++)
        if (vec[i] >= vec[i + 1])
            return false;

    return true;
}

int main(int argc, char const *argv[])
{
    TreeNode *head;
    BinaryTree bt;

    int arr[] = {15, 7, 16, 1, 12, 0, 0, 0, 2, 10, 14};
    head = bt.createBinaryTree(arr, head, 0, 11);

    cout << isBST(head);

    return 0;
}
