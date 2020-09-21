#include <iostream>
#include <stdlib.h>
#include "../utils/LinkedList.hpp"

using namespace std;

node *reverseList(node *head){
    if (!head || !head->next)
        return head;
    
    node *follow = nullptr;
    node *chead = head;
    head = head->next;
    while (head){
        chead->next = follow;
        follow = chead;
        chead = head;
        head = head->next;
    }
    chead->next = follow;
    
    return chead;   
}

int main(int argc, char const *argv[])
{
    LinkedList ll;
    node *head;
    int arr[] = {4, 1, 6, 5, 3, 4, 2, 2};
    head = ll.loadList(arr, 8);

    head = reverseList(head);

    while (head)
    {
        cout<<head->val<<" ";
        head = head->next;
    }
    
    return 0;
}




