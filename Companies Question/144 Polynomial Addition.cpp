/* Structure of Node used
struct Node
{
    int coeff;
    int pow;
    struct Node* next;
    
    Node(int c, int p){
        coeff = c;
        pow = p;
        next = NULL;
    }
    
};
*/

/* The below method print the required sum of polynomial
p1 and p2 as specified in output  */
Node* addPolynomial(Node *p1, Node *p2)
{
    Node *last = new Node(0, 0);
    Node *root = last;
    while(p1 && p2){
        if (p1->pow == p2->pow) {
            p1->coeff += p2->coeff;
            last->next = p1;
            p1 = p1->next;
            p2 = p2->next;
        } 
        else if(p1->pow > p2->pow) {
            last->next = p1;
            p1 = p1->next;
        }
        else {
            last->next = p2;
            p2 = p2->next;
        }
        last = last->next;
    }
    
    if (p1)
        last->next = p1;
    else
        last->next = p2;
    
    return root->next;
}
