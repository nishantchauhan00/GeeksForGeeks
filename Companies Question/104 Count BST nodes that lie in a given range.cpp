// brute force kind of technique - using preorder
void solver1(Node *head, int &n, int l, int h){
    if(!head)
        return;
    
    if (head->data >= l && head->data <= h)
        ++n;
    
    solver1(head->left, n, l, h);    
    solver1(head->right, n, l, h);    
}

// as its bst, take advantage and prune some path
void solver(Node *head, int &n, int l, int h){
    if(!head)
        return;
    
    if (head->data >= l && head->data <= h)
        ++n;

    if (head->data <= l) // only go right
        solver(head->right, n, l, h)
    else if (head->data > r) // only go left
        solver(head->left, n, l, h)
    else{
        solver(head->right, n, l, h)
        solver(head->left, n, l, h)
    }
}

int getCountOfNode(Node *root, int l, int h)
{
    int n = 0;
    solver(root, n, l, h);
    return n;
}