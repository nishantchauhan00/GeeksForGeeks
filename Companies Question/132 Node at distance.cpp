#include <iostream>
#include <algorithm>
#include <stack>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include "../utils/BinaryTree.hpp"
using namespace std;

/*
very bad method
return array containing only '1' from leaf node, increase each value by 1 at
every node

def printKDistantfromLeaf(root, k):
    ks = []
    def helper(head):
        if not head:
            return []
        if not head.left and not head.right:
            return [0]
        
        l_r = helper(head.left) + helper(head.right)
        
        for i in range(len(l_r)):
            l_r[i] += 1
        if k in l_r:
            ks.append(head)
        
        return l_r 

*/

void helper(TreeNode *root, int k, unordered_set<TreeNode *> &hset, vector<TreeNode *> vec)
{
    if (root == NULL) // null node(after leaf)
        return;

    vec.push_back(root);
    int i = vec.size() - k - 1;
    if (root->left == NULL && root->right == NULL && i >= 0) // leaf node
        hset.insert(vec[i]);
    
    helper(root->left, k, hset, vec);
    helper(root->right, k, hset, vec);
}

int printKDistantfromLeaf(TreeNode *root, int k)
{
    unordered_set<TreeNode *> hset;
    hset.clear();
    vector<TreeNode *> vec;
    vec.clear();
    helper(root, k, hset, vec);
    
    return hset.size();
}

int main()
{
    BinaryTree bt;
    TreeNode *root;

    int arr[] = {1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 8};
    root = bt.createBinaryTree(arr, root, 0, 13);

    int s = printKDistantfromLeaf(root, 2);
    cout << s << endl;

    return 0;
}
