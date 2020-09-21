#include <iostream>
#include <stdlib.h>
#include <vector>
#include "../utils/LinkedList.hpp"

using namespace std;


node* merge(node *head1, node *head2){
    if (!head1)
        return head2;
    if (!head2)
        return head1;
    
    if (head1->val > head2->val){
        head1->next = merge(head1->next, head2);
        return head1;
    }
    else{
        head2->next = merge(head1, head2->next);
        return head2;
    }
}


node *mergeSort(node *head){
    if(head==NULL || head->next==NULL)
        return head;

    // as in merge sort we have to divide list in two parts, 
    // so dividing the linked list here
    node *slow = head;
    node *fast = head->next;

    while(fast && fast->next){
        slow = slow->next;
        fast = fast->next->next;
    }

    node *nnode = slow->next;
    slow->next = nullptr;

    return merge(mergeSort(head), mergeSort(nnode));
}


int main(int argc, char const *argv[])
{
    LinkedList ll;
    node *head;
    int arr[] = {4, 1, 6, 5, 3, 4, 2, 2};
    head = ll.loadList(arr, 8);

    head = mergeSort(head);

    while (head)
    {
        cout<<head->val<<" ";
        head = head->next;
    }
    return 0;
}
