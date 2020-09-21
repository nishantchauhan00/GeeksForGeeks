/*
1. Store Inorder Traversal in vector
2. Make new Tree by recursively taking mid of the vector
*/

#include <iostream>
#include <stdlib.h>
#include <vector>
#include "../utils/BinaryTree.hpp"

using namespace std;

void inorder(TreeNode *root, vector<TreeNode *> &vec)
{
    if (root == nullptr)
        return;
    inorder(root->left, vec);
    vec.push_back(root);
    inorder(root->right, vec);
}

TreeNode *newbuildBalancedTree(int start, int end, vector<TreeNode *> &vec)
{
    if (start > end)
        return NULL;
    int mid = start + (end - start) / 2;
    TreeNode *nTreeNode = vec[mid];
    nTreeNode->left = newbuildBalancedTree(start, mid - 1, vec);
    nTreeNode->right = newbuildBalancedTree(mid + 1, end, vec);
    return nTreeNode;
}

TreeNode *buildBalancedTree(TreeNode *root)
{
    vector<TreeNode *> vec;
    inorder(root, vec);
    TreeNode *newtree = newbuildBalancedTree(0, vec.size(), vec);
    return newtree;
}

int main(int argc, char const *argv[])
{

    return 0;
}
