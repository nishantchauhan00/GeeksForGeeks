/*
Delete a given node in Linked List under given constraints

1) It must accept a pointer to the start node as the first parameter and node to be deleted as the second parameter i.e., a pointer to head node is not global.
2) It should not return a pointer to the head node.
3) It should not accept pointer to pointer to the head node.
*/

#include <iostream>
#include <stdlib.h>
#include <vector>
#include <queue>
#include "../utils/LinkedList.hpp"

using namespace std;

class Solution
{
public:
    void deleteNode(node *head, node *delnode)
    {
        if (head == delnode){
            if (head->next == nullptr)
                return;
                
            head->val = head->next->val;
            
            delnode = delnode->next;
            head->next = head->next->next;
            
            free(delnode);

            return;
        }

        node *head1 = head;
        while(head1->next){
            if (head1->next == delnode){
                break;
            }
            head1 = head1->next;
        }

        head1->next = head1->next->next;

        free(delnode);

        return;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    node *head;
    LinkedList ll;

    int arr[] = {1, 2, 3}; // 2 2
    head = ll.loadList(arr, 3);
    s.deleteNode(head, head);

    // int arr[] = {1, 2}; // 1 2
    // head = ll.loadList(arr, 2);
    // s.deleteNode(head, head->next);

    while(head){
        cout<<head->val<<"  ";
        head = head->next;
    }

    cout << endl;
    return 0;
}
