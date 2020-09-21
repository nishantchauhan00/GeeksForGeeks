#include <iostream>
#include <stdlib.h>
#include <vector>
#include <stack>
#include "../utils/BinaryTree.hpp"

using namespace std;

void inorder(TreeNode *root, vector<int> &vec)
{
    if (root == nullptr)
        return;
    inorder(root->left, vec);
    vec.push_back(root->val);
    inorder(root->right, vec);
}

/*this  function serializes 
the binary tree and stores 
it in the vector A*/
void serialize(TreeNode *root, vector<int> &A)
{
    if (!root)
    {
        A.push_back(-1);
        return;
    }

    A.push_back(root->val);
    serialize(root->left, A);
    serialize(root->right, A);
}

int i = 0;
TreeNode *deSerializeHelper(vector<int> &A, int n)
{
    if (i >= n || A[i] == -1)
    {
        i += 1;
        return nullptr;
    }

    TreeNode *head = new TreeNode(A[i]);
    // cout << i << " " << A[i] << " " << n << endl;

    i += 1;

    head->left = deSerializeHelper(A, n);
    head->right = deSerializeHelper(A, n);

    return head;
}

/*this function deserializes
 the serialized vector A*/
TreeNode *deSerialize(vector<int> &A)
{
    i = 0;
    TreeNode *head = deSerializeHelper(A, A.size());

    return head;
}

int main()
{
    BinaryTree bt;
    int arr[] = {10, 20, 30, 40, 60};

    TreeNode *root;
    root = bt.createBinaryTree(arr, root, 0, 5);

    vector<int> A;
    serialize(root, A);
    for (int x : A)
        cout << x << " ";
    cout << endl;

    TreeNode *newTreeRoot = deSerialize(A);
    A.clear();
    inorder(newTreeRoot, A);
    for (int x : A)
        cout << x << " ";
    cout << endl;

    return 0;
}