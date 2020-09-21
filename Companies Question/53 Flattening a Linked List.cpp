Node *merge(Node *h1, Node *h2)
{
    if (h1 == NULL)
        return h2;
    if (h2 == NULL)
        return h1;

    Node *merged_list;
    if (h1->data < h2->data)
    {
        merged_list = h1;
        merged_list->bottom = merge(h1->bottom, h2);
    }
    else
    {
        merged_list = h2;
        merged_list->bottom = merge(h1, h2->bottom);
    }
    return merged_list;
}


// list will be printed with bottom node not next node
Node *flatten(Node *root)
{
    Node *a = root;
    Node *b = root->next;
    while (b != NULL)
    {
        Node *c = b->next;
        // we merge list one by one and then update both into one
        a = merge(a, b); 
        b = c;
    }
    return a;
}

/*
.
.
method 2
.
.
brute force way - creating new list
.
Node flatten(Node root)
    {
    // Your code here
    PriorityQueue<Integer> queue = new PriorityQueue<>();
    
    // upper_main remains on upper list while traveller travels on all nodes
    Node upper_main = root;
    Node traveller = root;
    while(upper_main != null){
        while(traveller != null){
            queue.add(traveller.data);
            traveller = traveller.bottom;
        }
        upper_main = upper_main.next;
        traveller = upper_main;
    }

    Node temp = new Node(queue.poll());
    Node head = temp;
    while(!queue.isEmpty()){
        Node curr = new Node(queue.poll());
        temp.bottom = curr;
        temp = curr;
    }

    return head;
}
*/