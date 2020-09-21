#include <iostream>
#include <stdlib.h>
#include <vector>
#include <queue>
#include "../utils/LinkedList.hpp"

using namespace std;

class Solution
{
public:
    int nthNodeLinkedList1(node *head, int n) // time: O(n)   space: O(n)
    {
        vector<int> out;
        while (head)
        {
            out.push_back(head->val);
            head = head->next;
        }

        if (n < 1 || n > out.size())
            return -1;

        return out[out.size() - n];
    }

    int nthNodeLinkedList(node *head, int n) // time: O(n)   space: O(m), m <= n
    {
        queue<int> out;
        while (head)
        {
            out.emplace(head->val);
            if (out.size() > n)
                out.pop();
            head = head->next;
        }

        if (n < 1 || n > out.size())
            return -1;

        return out.front();
    }

    int nthNodeLinkedList2(node *head, int n) 
    {
        /*
        h1 = head
        h2 = head->next
        now traverse at double speed
        while h1 or h2:
            out.append(h1->val)
            out.append(h2->val)

            h1 = h1->next->next
            h2 = h2->next->next
        but there will be lots of checking in between

        another approach, we can maintain 2 pointer, so O(n) time with O(1) space
        */
        return -1;
    }
};

int main(int argc, char const *argv[])
{
    LinkedList ll;
    node *head;
    Solution s;
    // int arr[] = {1, 2, 3, 4, 5, 6}; // 0 -1
    // int arr[] = {1, 2, 3, 4, 5, 6}; // 1 6
    // head = ll.loadList(arr, 6);
    // cout << s.nthNodeLinkedList(head, 0);

    // int arr[] = {1, 2, 3, 5, 6}; // 3 3
    // head = ll.loadList(arr, 5);
    // cout<<s.nthNodeLinkedList(head, 3);

    // int arr[] = {1, 2, 3}; // 2 2
    // head = ll.loadList(arr, 3);
    int arr[] = {1, 2}; // 1 2
    head = ll.loadList(arr, 2);
    cout << s.nthNodeLinkedList(head, 1);

    cout << endl;
    return 0;
}
