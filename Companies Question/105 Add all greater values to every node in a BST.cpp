static long long until = 0;
void rider(Node *root){
    if(!root)
        return;
    
    rider(root->right);
    
    root->data += until;
    until = root->data;
    
    rider(root->left);
}

Node* modify(Node *root)
{
    Node *croot = root;
    until = 0;
    rider(root);
    return croot;
}