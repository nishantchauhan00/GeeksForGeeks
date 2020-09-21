#include <iostream>
#include <stdlib.h>
#include <vector>
#include "../utils/LinkedList.hpp"

using namespace std;

class Solution
{
public:
    node *pairwise_swap(node *head)
    {
        node *chead = head;
        while (head && head->next)
        {
            // cout<<head->val<<head->next->val<<endl;
            int temp = head->val;
            head->val = head->next->val;
            head->next->val = temp;
            head = head->next->next;
        }
        return chead;
    }
};

int main(int argc, char const *argv[])
{
    LinkedList ll;
    node *head;
    int arr[] = {1, 2, 3, 4, 5, 6}; // 2 1 4 3 6 5
    head = ll.loadList(arr, 6);
    // int arr[] = {1, 2, 3, 5, 6}; // 2 1 5 3 6
    // head = ll.loadList(arr, 5);
    // int arr[] = {1, 2, 3}; // 2 1 3
    // head = ll.loadList(arr, 3);
    // int arr[] = {1, 2}; // 2 1
    // head = ll.loadList(arr, 2);
    Solution s;
    node *outhead = s.pairwise_swap(head);
    while (outhead)
    {
        cout << outhead->val << " ";
        outhead = outhead->next;
    }

    return 0;
}
