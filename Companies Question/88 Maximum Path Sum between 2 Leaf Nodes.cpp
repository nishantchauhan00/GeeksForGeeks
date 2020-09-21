#include <iostream>
#include <stdlib.h>
#include <vector>
#include "../utils/BinaryTree.hpp"
#define INT_MIN -2147483647
using namespace std;

int getMax(TreeNode *head, int &result)
{
    // on null node we return int_min, on leaf node, we cant compare only one
    // node so we return node value
    if (!head)
        return INT_MIN;
    else if (!head->left && !head->right) // leaf node
        return head->val;

    int l = getMax(head->left, result);
    int r = getMax(head->right, result);

    if (head->left && head->right)
        result = max(result, l + r + head->val);

    return max(l, r) + head->val;
}

int maxPathSum(TreeNode *root)
{
    int result = INT_MIN;
    getMax(root, result);
    return result;
}

int main(int argc, char const *argv[])
{
    TreeNode *head;
    BinaryTree bt;

    int arr[] = {3, 4, 5, -10, 4};
    head = bt.createBinaryTree(arr, head, 0, 5);
    // 16

    cout << maxPathSum(head) << endl;

    return 0;
}
