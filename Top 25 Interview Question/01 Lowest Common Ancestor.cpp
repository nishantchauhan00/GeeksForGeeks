#include <iostream>
#include <vector>
#include <stdlib.h>
#include "../utils/BinaryTree.hpp"

using namespace std;

class Solution
{
public:
    TreeNode *findLCA(TreeNode *root, int n1, int n2)
    {
        if (root == NULL)
            return nullptr;

        // If either n1 or n2 matches with root's key, report
        // the presence by returning root (Note that if a key is
        // ancestor of other, then the ancestor key becomes LCA
        if (root->val == n1 || root->val == n2)
            return root;

        // Look for keys in left and right subtrees
        TreeNode *left_lca = findLCA(root->left, n1, n2);
        TreeNode *right_lca = findLCA(root->right, n1, n2);

        // If both of the above calls return Non-NULL, then one key
        // is present in once subtree and other is present in other,
        // So this node is the LCA
        if (left_lca && right_lca)
            return root;

        // Otherwise check if left subtree or right subtree is LCA
        return (left_lca != NULL) ? left_lca : right_lca;
    }

    int findLCA1(TreeNode *head, int x, int y)
    {
        vector<int> xvec;
        vector<int> yvec;
        TreeNode *chead = head;
        if (!(findNodes(chead, xvec, x) && findNodes(chead, yvec, y)))
            return -1;

        // for (int i = 0; i < xvec.size(); i++)
        //     cout << xvec[i] << " ";
        // cout <<endl;

        // for (int i = 0; i < yvec.size(); i++)
        //     cout << yvec[i] << " ";
        // cout <<endl;

        int i = 0;
        for (i = 0; i < min(xvec.size(), yvec.size()); i++)
        {
            if (xvec[i] != yvec[i])
                break;
        }
        return xvec[i - 1];
    }

    bool findNodes(TreeNode *head, vector<int> &vec, int matchval)
    {
        if (head == nullptr)
            return false;

        vec.push_back(head->val);

        if (head->val == matchval)
            return true;

        // search left and right
        if ((head->left && findNodes(head->left, vec, matchval)) || (head->right && findNodes(head->right, vec, matchval)))
            return true;

        vec.pop_back(); // if not found in any case
        return false;
    }
};

int main(int argc, char const *argv[])
{
    TreeNode *head;
    BinaryTree bt;
    Solution s;

    int arr[] = {1, 2, 3, 4, 5, 6, 7};
    head = bt.createBinaryTree(arr, head, 0, 7);
    cout << s.findLCA(head, 4, 5)->val << endl;
    cout << s.findLCA(head, 4, 6)->val << endl;
    cout << s.findLCA(head, 3, 4)->val << endl;
    cout << s.findLCA(head, 2, 4)->val << endl;
    // 2   1   1   2

    return 0;
}
