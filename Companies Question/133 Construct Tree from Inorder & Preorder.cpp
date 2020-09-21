/*
Node is as follows:
struct Node
{
  int data;
  Node* left;
  Node* right;
};

Example 1:
Input:
N = 4
inorder[] = {1 6 8 7}
preorder[] = {1 6 7 8}
Output: 8 7 6 1

Example 2:
Input:
N = 6
inorder[] = {3 1 4 0 5 2}
preorder[] = {0 1 3 4 2 5}
Output: 3 4 1 5 2 0
Explanation: The tree will look like
       0
    /     \
   1       2
 /   \    /
3    4   5


just find the index of node in inorder, divide the preorder for next traversal
according to that index, inorder can be divided directly with that index

we need to find only in that range
if index out of range then return null
*/
Node *helper(int in[],int pre[], int l, int h, int preindex, int n){
    if (l > h)
        return nullptr;
    
    Node *nnode = new Node(pre[preindex]);
    
    int i = l;
    for(;i<=h && in[i] != pre[preindex]; ++i);
    
    nnode->left = helper(in, pre, l, i-1, preindex+1, n);
    nnode->right = helper(in, pre, i+1, h, preindex+i-l+1, n);
    
    return nnode;
}

Node* buildTree(int in[],int pre[], int n)
{
    return helper(in, pre, 0, n-1, 0, n);
}