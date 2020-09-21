// function should print the topView of the binary tree
void topView(struct Node *root)
{
    map<int, int> topnode;
    queue<Node *> qnode;
    queue<int> m;
    int hd = 0, n = 1;
    
    qnode.push(root);
    m.push(0);
    
    while(!qnode.empty())
    {
        Node *temp = qnode.front();
        int col = m.front();
        qnode.pop();
        m.pop();
        
        // if not occured before, then insert
        if (topnode.find(col) == topnode.end())
            topnode[col] = temp->data;
        
        // push left and right node in qnode
        // push the column number w.r.t. top root in 'm'
        if (temp->left){
            qnode.push(temp->left);
            m.push(col - 1);
        }
        if (temp->right){
            qnode.push(temp->right);
            m.push(col + 1);
        }
    }
    
    for (auto it = topnode.begin(); it != topnode.end(); it++)
        printf("%d ", it->second);
}
