#include <iostream>
#include <stdlib.h>
#include <vector>
#include "../utils/BinaryTree.hpp"

using namespace std;

TreeNode *invert(TreeNode *root)
{
    if (root == nullptr)
        return NULL;

    TreeNode *left = invert(root->left);
    TreeNode *right = invert(root->right);
    root->left = right;
    root->right = left;

    return root;
}

// or, both are same at core, but it doent return anything
 
void mirror(TreeNode *head)
{
    if (head == NULL)
    {
        return;
    }
    else
    {
        mirror(head->left);
        mirror(head->right);
        TreeNode *temp = head->left;
        head->left = head->right;
        head->right = temp;
    }
}

int main(int argc, char const *argv[])
{
    TreeNode *head;
    BinaryTree bt;

    int arr[] = {1, 3, 2, 0, 0, 5, 4};
    head = bt.createBinaryTree(arr, head, 0, 7);

    head = invert(head);

    bt.levelOrder(head);

    return 0;
}
