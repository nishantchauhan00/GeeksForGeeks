#include <iostream>
#include <map>
#include <string.h>
#include "../utils/BinaryTree.hpp"
using namespace std;

bool checkIdentical(TreeNode *root, TreeNode *node)
{
    if (root == NULL && node == NULL)
        return true;
    if (root == NULL || node == NULL)
        return false;
    if (root->data != node->data)
        return false;
    return checkIdentical(root->left, node->left) && checkIdentical(root->right, node->right);
}

bool traversal(TreeNode *root, map<int, TreeNode *> &m)
{
    if (root == NULL)
        return false;

    int temp = root->data;
    if (m.find(temp) != m.end())
    {
        TreeNode *node = m[temp];
        if (node->left == NULL && node->right == NULL) // leaf case
            return false;
        if (checkIdentical(node, root))
            return true;
    }

    m[root->data] = root;
    bool left = traversal(root->left, m);
    bool right = traversal(root->right, m);

    return left | right; // if any side gives true
}

bool dupSub(TreeNode *root)
{
    map<int, TreeNode *> m;
    return traversal(root, m);
}

int main(int argc, char const *argv[])
{
    BinaryTree bt;
    TreeNode *root, *root1;

    // int arr[] = {1, 2, 3, 4, 5, 0, 2, 0, 0, 0, 0, 0, 0, 4, 5};
    // root = bt.createBinaryTree(arr, root, 0, 15);

    int arr[] = {1, 2, 3, 4, 5, 6, 7};
    root = bt.createBinaryTree(arr, root, 0, 7);

    cout << boolalpha << dupSub(root) << endl;

    return 0;
}
