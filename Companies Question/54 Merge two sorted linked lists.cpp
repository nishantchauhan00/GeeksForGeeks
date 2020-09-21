// although it can be done more efficiently
// but we did it for good explanation
Node *merge(Node *h1, Node *h2)
{
    if (!h1)
        return h2;
    if (!h2)
        return h1;

    Node *merged_list = new Node(0);
    if (h1->data < h2->data)
    {
        merged_list->data = h1->data;
        merged_list->next = merge(h1->next, h2);
    }
    else
    {
        merged_list->data = h2->data;
        merged_list->next = merge(h1, h2->next);
    }
    return merged_list;
}

Node *sortedMerge(Node *head_A, Node *head_B)
{
    return merge(head_A, head_B);
}