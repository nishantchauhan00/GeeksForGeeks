/*
Structure of the node of the list is as
struct Node
{
	int data;
	struct Node *next, *prev;
	Node (int x){
	    data = x;
	    next = prev = NULL;
	}
}; */

// Function to merge two DLLs
Node *split(Node *head)
{
    Node *slow = head, *fast = head->next;
    while (fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    Node *temp = slow->next;
    slow->next = NULL;
    return temp;
}

Node *merge(Node *a, Node *b)
{
    if (a == NULL)
        return b;
    if (b == NULL)
        return a;

    Node *head, *tail;
    if (a->data < b->data)
    {
        head = tail = a;
        a = a->next;
    }
    else
    {
        head = tail = b;
        b = b->next;
    }

    while (a != NULL && b != NULL)
    {
        if (a->data < b->data)
        {
            tail->next = a;
            tail = a;
            a = a->next;
        }
        else
        {
            tail->next = b;
            tail = b;
            b = b->next;
        }
    }

    if (a != NULL)
        tail->next = a;
    else
        tail->next = b;

    Node *currnode = head, *prevnode = NULL;
    while (currnode != NULL)
    {
        currnode->prev = prevnode;
        prevnode = currnode;
        currnode = currnode->next;
    }

    return head;
}

void MergeSort(Node **headref)
{
    Node *head = *headref;
    if (head == NULL || head->next == NULL)
        return;

    Node *a = head;
    Node *b = split(head);

    MergeSort(&a);
    MergeSort(&b);
    *headref = merge(a, b);
}

struct Node *sortDoubly(struct Node *head)
{
    MergeSort(&head);
    return head;
}