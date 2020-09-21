#include <iostream>
#include <stdlib.h>
#include <vector>
#include "../utils/LinkedList.hpp"

using namespace std;

node *reverselist(node *head, int k){
    int arr[k] = {-1};
    node *chead = head;
    node *chead2 = head;

    while (chead){
        for(int i=0; i<k && chead; i++){
            arr[i] = chead->val;
            chead = chead->next;
        }

        int n = k;
        while(arr[n-1] == -1)
            n -= 1;

        for(int i=0; i<n && chead2; i++){
            chead2->val = arr[n-i-1];
            arr[k-i-1] = -1;
            chead2 = chead2->next;
        }
    }

    return head;        
}

int main(int argc, char const *argv[])
{
    LinkedList ll;
    node *head;

    int arr[] = {1, 2, 3, 4, 5};
    head = ll.loadList(arr, 5);
    head = reverselist(head, 3);
    // 3 2 1 5 4

    // int arr[] = {1, 2, 2, 4, 5, 6, 7, 8};
    // head = ll.loadList(arr, 8);
    // head = reverselist(head, 4);
    // // 4 2 2 1 8 7 6 5


    while (head)
    {
        cout<<head->val<<" ";
        head = head->next;
    }
    
    return 0;
}




