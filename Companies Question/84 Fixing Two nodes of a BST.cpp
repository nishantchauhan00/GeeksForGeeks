#include <iostream>
#include <algorithm>
#include <vector>
#include "../utils/BinaryTree.hpp"
using namespace std;
#define INT_MAX 2147483647

void inorder(TreeNode *root, TreeNode *&prev, TreeNode *&node1, TreeNode *&node2)
{
    if (!root)
        return;

    inorder(root->left, prev, node1, node2);

    if (prev && prev->val > root->val)
    {
        if (!node1)
        {
            node1 = prev;
            node2 = root;
        }
        else
            node2 = root;
    }

    prev = root;

    inorder(root->right, prev, node1, node2);
}

void swap(int *r, int *s)
{
    int temp = *r;
    *r = *s;
    *s = temp;
}

TreeNode *correctBST(TreeNode *root)
{
    TreeNode *prev = NULL, *node1 = NULL, *node2 = NULL;

    inorder(root, prev, node1, node2);

    // swapping pointers not values, because in real life data can be huge
    // so instead of data, swapping the pointers to data is better
    swap(node1->val, node2->val);

    return root;
}

int main(int argc, char const *argv[])
{
    BinaryTree bt;
    TreeNode *root;

    int arr[] = {10, 5, 8, 2, 20};
    root = bt.createBinaryTree(arr, root, 0, 5);

    // int arr[] = {11, 3, 17, 0, 4, 10};
    // root = bt.createBinaryTree(arr, root, 0, 6);

    root = correctBST(root);
    // 10  5  20  2  8
    bt.inorder(root);

    return 0;
}
