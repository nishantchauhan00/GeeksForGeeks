/* Structure for tree and linked list

struct Node
{
    int data;
    struct Node* left;
    struct Node* right;
    
    Node(int x){
        data = x;
        left = right = NULL;
    }
};
 */

// This function should return head to the DLL(double linked list)
void inorder(Node *head, deque<Node *> &qu){
    if (head == NULL)
        return;
    
    inorder(head->left, qu);
    qu.push_back(head);
    inorder(head->right, qu);
}


Node * bToDLL(Node *root)
{
    // if no root or its just a single node present in tree
    if (root == NULL || (root->left == NULL && root->right == NULL))
        return root;
        
    deque<Node *> qu;
    qu.clear();
    inorder(root, qu);
    
    Node *temp1 = qu.front(), *temp2;
    root = temp1;
    qu.pop_front();
    while (!qu.empty()) {
        temp2 = qu.front();
        temp1->right = temp2;
        temp2->left = temp1;
        temp1 = temp2;
        qu.pop_front();
    }
    
    return root;
}