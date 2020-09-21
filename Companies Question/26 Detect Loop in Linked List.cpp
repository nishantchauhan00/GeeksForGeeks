#include <iostream>
#include <stdlib.h>
#include <unordered_set>
#include "../utils/LinkedList.hpp"

using namespace std;

// if loop exists, two nodes meet again if there are at different speeds, 
// otherwise null/end is reached
bool detectLoop1(node *head)
{
    node *slow = head;
    node *fast = head->next;
    while (fast && fast->next)
    {
        // cout<<slow->val<<" "<<fast->val<<" "<<fast->next->data<<endl;
        if (slow == fast)
            return true;
        slow = slow->next;
        fast = fast->next->next;
    }
    return false;
}

// O(n) time complexity
bool detectLoop2(node *head)
{
    unordered_set<node *> nodelist;
    while (head)
    {
        // cout<<slow->val<<" "<<fast->val<<" "<<fast->next->val<<endl;
        if (nodelist.find(head) != nodelist.end())
            return true;
        nodelist.insert(head);
        head = head->next;
    }
    return false;
}

// O(1) time complexity, choose a value which is not in any node like 0, -1, 
// -99999, NULL(if allowed), then if that value strikes again, there is a loop
bool detectLoop(node *head)
{
    while (head)
    {
        // cout<<slow->val<<" "<<fast->val<<" "<<fast->next->val<<endl;
        if (head->val == -1)
            return true;
        head->val = -1;
        head = head->next;
    }
    return false;
}

int main(int argc, char const *argv[])
{
    LinkedList ll;
    node *head;

    int arr[] = {1, 2, 3, 4, 5, 3, 6};
    head = ll.loadList(arr, 5);

    head->next->next->next->next->next = head->next->next;

    cout << boolalpha << detectLoop(head);

    return 0;
}
