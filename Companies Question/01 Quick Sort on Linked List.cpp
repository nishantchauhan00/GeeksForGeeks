#include <iostream>
#include <stdlib.h>
#include <vector>
#include "../utils/LinkedList.hpp"

using namespace std;

node* tail(node *head){
    node *current = head;
    while(current->next != NULL) current = current->next;
    return current;
}

void swap_value(node * first, node * second){
    int temp = first->data;
    first->data = second->data;
    second->data = temp;
}

node * partition(node *head, node *tail){
    node * i=head, *j=head->next;
    node *pivot = head;
    while(j != tail->next){
        if(j->data < pivot->data){
            swap_value(i->next,j);
            i = i->next;
        }
        j = j->next;
    }

    swap_value(pivot,i);
    return i;
}

void quickSortRec(node * head, node *tail){
    if(head == tail) return;
    if(tail == NULL || head == NULL) return;

    node * pivot = partition(head , tail);

    quickSortRec(head, pivot);
    quickSortRec(pivot->next, tail);
}

void quickSort(node *headRef) {
    quickSortRec(headRef, tail(headRef));
}



int main(int argc, char const *argv[])
{
    LinkedList ll;
    node *head;
    int arr[] = {4, 1, 6, 5, 3, 4, 2, 2};
    head = ll.loadList(arr, 8);

    head = quickSort(head);

    while (head)
    {
        cout<<head->val<<" ";
        head = head->next;
    }
    

    return 0;
}
