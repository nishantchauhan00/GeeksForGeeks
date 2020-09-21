void swap(Node *a, Node *b){
    int temp = a->data;
    a->data = b->data;
    b->data = temp;
}

/* a Node of the doubly linked list */
/*
struct Node
{
    int data;
    struct Node *next;
    struct Node *prev;
    
    Node(int x){
        data = x;
        next = NULL;
        prev = NULL;
    }
};
*/
Node* partition(Node *low, Node *high){
    int pivot = high->data; // taking last node as pivot
    Node *i = low; // for tracking index of values less than pivot
    while (low != high){
        if (low->data < pivot){
            swap(i, low);
            i = i->next;
        }
        low = low->next;
    }
    
    // last swap 
    swap(i, high);
    
    return i;
}


void quickSort(Node *low, Node *high){
    if (low != high && low != high->next){
        Node *p = partition(low, high);
        quickSort(low, p->prev);
        quickSort(p->next, high);
    }
}

