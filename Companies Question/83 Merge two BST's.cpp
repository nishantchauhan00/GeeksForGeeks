#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include "../utils/BinaryTree.hpp"
using namespace std;

#define INT_MAX 2147483647

void inorder(TreeNode *head, vector<int> &viewarr)
{
    if (!head)
        return;
    inorder(head->left, viewarr);
    viewarr.push_back(head->val);
    inorder(head->right, viewarr);
}

// method 1 - 0.17s
vector<int> merge1(TreeNode *root1, TreeNode *root2)
{
    vector<int> viewarr;
    inorder(root1, viewarr);
    inorder(root2, viewarr);
    sort(viewarr.begin(), viewarr.end());
    return viewarr;
}

// method 2 - 0.10s
vector<int> merge2(TreeNode *root1, TreeNode *root2)
{
    vector<int> viewarr1, viewarr2;
    inorder(root1, viewarr1);
    inorder(root2, viewarr2);

    int i = 0, j = 0, k = 0, n1 = viewarr1.size(), n2 = viewarr2.size();
    vector<int> out(n1 + n2);
    while (i < n1 && j < n2)
        out[k++] = viewarr1[i] < viewarr2[j] ? viewarr1[i++] : viewarr2[j++];
    while (i < n1)
        out[k++] = viewarr1[i++];
    while (j < n2)
        out[k++] = viewarr2[j++];

    return out;
}

// method 3 - 0.12s
// as in questions it asks to use limited space, so in this space will be
// limited every time
void pushLeft(TreeNode *root, stack<TreeNode *> &s)
{
    // pushes all left of the node including the input node
    while (root)
    {
        s.push(root);
        root = root->left;
    }
}

vector<int> merge(TreeNode *root1, TreeNode *root2)
{
    vector<int> out;
    stack<TreeNode *> s1, s2;
    pushLeft(root1, s1);
    pushLeft(root2, s2);

    while (!s1.empty() || !s2.empty())
    {
        int a = !s1.empty() ? s1.top()->val:INT_MAX;
        int b = !s2.empty() ? s2.top()->val:INT_MAX;

        if (a <= b)
        {
            out.push_back(a);
            TreeNode *topnode = s1.top();
            s1.pop();
            // insert all left nodes of right of popped nodes(including right node)
            pushLeft(topnode->right, s1);
        }
        else
        {
            out.push_back(b);
            TreeNode *topnode = s2.top();
            s2.pop();
            pushLeft(topnode->right, s2);
        }
    }
    return out;
}

int main(int argc, char const *argv[]){
    BinaryTree bt;
    TreeNode *root, *root1;

    int arr[] = {2, 1, 3, 0, 0, 0, 7};
    root = bt.createBinaryTree(arr, root, 0, 7);

    int arr1[] = {5, 3, 6, 2, 4};
    root1 = bt.createBinaryTree(arr1, root1, 0, 5);

    vector<int> viewarr;
    viewarr = merge(root, root1); // it should be in ascending order

    for (int x : viewarr)
        cout << x << " ";

    return 0;
}
