Node* insert(Node* root, int key)
{
    Node* head = root;
    while (true) {
        if (head->data == key)
            break;
        else if (head->data > key) {
            if (!head->left)
                head->left = new Node(key);
            head = head->left;
        }
        else {
            if (!head->right)
                head->right = new Node(key);
            head = head->right;
        }
    }
    return root;
}



