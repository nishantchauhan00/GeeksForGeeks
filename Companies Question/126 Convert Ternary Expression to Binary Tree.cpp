/*Complete the function below
Node is as follows
struct Node{
	char data;
	Node *left,*right;
};
*/
Node *convertExpression(string str,int j) {
    Node *root = new Node(str[0]);
    Node *croot = root;
    stack<Node *> st;
    int i = 2;
    
    while(i < str.size()){
        Node* nnode = new Node(str[i]);
        if (str[i-1] == '?'){
            st.push(root);
            root = st.top();
            st.push(nnode);
            root->left = nnode;
            root = root->left;
        } else {
            root = st.top();
            st.pop();
            root->right = nnode;
            root = root->right;
        }
        i += 2;
    }
        
    return croot;
}
