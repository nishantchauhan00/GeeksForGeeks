#include <iostream>
#include <stdlib.h>
#include <vector>
#include <stack>
#include "../utils/LinkedList.hpp"

using namespace std;

node *getMid(node *head)
{
    node *mid = head, *last = head;
    while (last && last->next)
    {
        mid = mid->next;
        last = last->next->next;
    }
    return mid;
}

void reorderList1(node *head)
{
    node *mid = getMid(head);

    // making last of list-1 = nullptr
    node *temp = mid;
    mid = mid->next;
    temp->next = nullptr;
    stack<node *> aftermid;
    // filling stack with nodes after mid
    while (mid)
    {
        aftermid.push(mid);
        mid = mid->next;
    }

    // rearranging
    node *head2 = head, *nextnode = head;
    while (!aftermid.empty())
    {
        head2 = nextnode;
        nextnode = head2->next;
        node *nn = aftermid.top();
        aftermid.pop();
        head2->next = nn;
        nn->next = nextnode;
    }
}

void reorderList(node *head)
{
    if(!head || !head->next || !head->next->next)
        return;

    node *mid = getMid(head);

    // making last of list-1 = nullptr
    node *temp = mid;
    mid = mid->next;
    temp->next = NULL;

    // reversing the list after mid
    node *nextnode = mid->next;
    temp = mid;
    mid->next = nullptr;
    while (nextnode)
    {
        temp = nextnode->next;
        nextnode->next = mid;
        mid = nextnode;
        nextnode = temp;
    }
    // now mid is first node of reversed list-2(points to last node)

    // rearranging
    node *head2 = head, *temp2;
    while (head2 && mid)
    {
        temp = head2->next;
        temp2 = mid->next;

        head2->next = mid;
        mid->next = temp;

        head2 = temp;
        mid = temp2;
    }
}

int main(int argc, char const *argv[])
{
    LinkedList ll;
    node *head;
    int arr[] = {1, 2, 3, 4, 5};
    head = ll.loadList(arr, 5);

    reorderList(head);

    // 1 5 2 4 3
    while (head)
    {
        cout << head->val << " ";
        head = head->next;
    }
    return 0;
}
