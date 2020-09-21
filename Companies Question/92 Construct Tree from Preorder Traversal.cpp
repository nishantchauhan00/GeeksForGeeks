/*
Input :      
N = 5
pre[] = {10, 30, 20, 5, 15}
preLN[] = {N, N, L, L, L}

Output:
          10
        /    \
      30      15
     /  \     
   20    5   
*/

static int i = 0;
Node *createTree(int n, int pre[], char preLN[]){
    if (i >= n)
        return NULL;
    
    Node *nnode = new Node(pre[i]);
    
    if (preLN[i++] == 'N'){
        nnode->left = createTree(n, pre, preLN);
        nnode->right = createTree(n, pre, preLN);
    }
    
    return nnode;
}

struct Node *constructTree(int n, int pre[], char preLN[])
{
    i = 0;
    return createTree(n, pre, preLN);
}