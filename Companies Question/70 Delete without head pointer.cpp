#include <iostream>
#include <stdlib.h>
#include "../utils/LinkedList.hpp"

using namespace std;

// by shifting the values 1 ahead and making last second next node = null
// wont work if it is last node or null, but in question we are given
// contraint that it will not be last node
void deleteNode1(node *head)
{
    node *temp = head;
    while (head->next){
        head->val = head->next->val;
        temp = head;
        head = head->next;
    }
    temp->next = nullptr;
}

// highly efficient,  beauty of pointers
void deleteNode(node *head){
    // head->val = head->next->val;
    // head->next = head->next->next;
    /* or, we are given with pointer to node(head), we just make current
       node(*head) equal to next node(*head->next).
       Although it will work as it is, We also take care of memory leak here*/
    node *temp = head->next; 
    *head = *head->next;
    delete temp; 
}


int main(int argc, char const *argv[])
{
    LinkedList ll;
    node *head;

    int arr[] = {1, 2, 3, 4, 5, 3, 6};
    head = ll.loadList(arr, 7);

    // node to deleted: 3rd node
    deleteNode(head->next->next);

    while (head)
    {
        cout << head->val<<"  ";
        head = head->next;
    }

    return 0;
}
