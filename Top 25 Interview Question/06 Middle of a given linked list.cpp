#include <iostream>
#include <stdlib.h>
#include <vector>
#include "../utils/LinkedList.hpp"

using namespace std;

class Solution
{
public:
    vector<int> middleLinkedList(node *head)
    {
        vector<int> out;
        node *head1 = head, *head2 = head;
        while (head2)
        {
            // cout << head1->val << " " << head2->val << endl;
            if (head2->next && head2->next->next)
            {
                head1 = head1->next;
                head2 = head2->next->next;
            }
            else
            {
                out.push_back(head1->val);
                if (head2->next)
                    out.push_back(head1->next->val);
                break;
            }
        }
        return out;
    }
};

int main(int argc, char const *argv[])
{
    LinkedList ll;
    node *head;
    // int arr[] = {1, 2, 3, 4, 5, 6}; // 3 4
    // head = ll.loadList(arr, 6);
    // int arr[] = {1, 2, 3, 5, 6}; // 3
    // head = ll.loadList(arr, 5);
    int arr[] = {1, 2, 3}; // 2
    head = ll.loadList(arr, 3);
    // int arr[] = {1, 2}; // 1 2
    // head = ll.loadList(arr, 2);
    Solution s;
    vector<int> out = s.middleLinkedList(head);
    for (int x : out)
        cout << x << " ";

    return 0;
}
