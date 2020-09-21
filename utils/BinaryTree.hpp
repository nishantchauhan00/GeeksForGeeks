#include <stdlib.h>
#include <iostream>
#include <queue>
using namespace std;
#define BinaryTree_H

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class BinaryTree
{
public:
    TreeNode *createBinaryTree(int arr[], TreeNode *root, int i, int n)
    {
        if (arr[i] == 0)
        {
            return NULL;
        }
        if (i < n)
        {
            TreeNode *temp = new TreeNode(arr[i]);
            root = temp;
            root->left = createBinaryTree(arr, root->left, 2 * i + 1, n);
            root->right = createBinaryTree(arr, root->right, 2 * i + 2, n);
        }
        return root;
    }

    void preorder(TreeNode *p)
    {
        if (p)
        {
            cout << p->val << " ";
            preorder(p->left);
            preorder(p->right);
        }
    }
    void inorder(TreeNode *p)
    {
        if (p)
        {
            inorder(p->left);
            cout << p->val << " ";
            inorder(p->right);
        }
    }
    void postorder(TreeNode *p)
    {
        if (p)
        {
            postorder(p->left);
            postorder(p->right);
            cout << p->val << " ";
        }
    }
    void levelOrder(TreeNode *root)
    {
        queue<TreeNode *> q;
        q.push(root);
        while (!q.empty())
        {
            TreeNode *t = q.front();
            q.pop();
            cout<<t->val<<" ";
            if (t->left)
                q.push(t->left);
            if (t->right)
                q.push(t->right);
        }
    }
};