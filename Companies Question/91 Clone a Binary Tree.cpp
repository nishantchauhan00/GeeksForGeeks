/* A binary tree node has data, pointer to left child
   and a pointer to right child 
struct Node
{
    int data;
    Node* left;
    Node* right;
    Node *random;
};
*/

/* The function should clone the passed tree and return 
   root of the cloned tree */
Node* cloneTree1(Node* tree) // LOL:}}
{
    Node *root;
    *root=*tree;
    return root;
}

Node* helper(Node* tree, map<Node*,Node*>mp){
    if(!tree)
        return NULL;
    if(mp.find(tree)!=mp.end())
        return tree;
    else{
        Node* root= new Node(tree->data);
        mp[tree] = root;
        root->left = helper(tree->left,mp);
        root->right = helper(tree->right,mp);
        root->random = helper(tree->random,mp);
        return root;
    }
}

// map here helps in keeping track if the node have been made before
// or not, it is done due to a random pointer is present with each node
// if node is made then it is returned otherwise we make it and fill all values
// or data of a node structure provided
Node* cloneTree(Node* tree)
{
    map<Node*,Node*> mp;
    return helper(tree,mp);
}