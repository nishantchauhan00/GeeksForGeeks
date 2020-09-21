#include <iostream>
#include <stdlib.h>
#include <unordered_set>
#include <stack>
#include "../utils/LinkedList.hpp"
#define INT_MIN -999999
using namespace std;

// 0.69s,  O(n) time and O(n) space
void removeLoop1(node *head)
{
    unordered_set<node *> hset;
    while (head && hset.find(head->next) == hset.end())
    {
        hset.insert(head);
        head = head->next;
    }

    if (head)
        head->next = nullptr;
}

// lets cheat, bad solution
// this solution takes advantage of given constraint that it will only have
// values >= 0
// 0.3s
void removeLoop2(node *head)
{
    node *prev = head, *chead = head;

    while (head)
    {
        head->val = (head->val == 0) ? INT_MIN : (-1 * head->val);

        if (head->val < 0)
        {
            prev->next = nullptr;
            break;
        }
        head = head->next;
    }

    // restoring values
    while (chead)
    {
        chead->val *= (chead->val == INT_MIN) ? 0 : -1;
        chead = chead->next;
    }
}

/*
good solution

1. Use the Hare Tortoise algorithm to find out if there is a loop
2. Next, find the size of the loop. Make one pointer stay at the meeting point 
   of Hare Tortoise and use the other pointer to complete one round around the 
   loop. Count the steps required to cover the loop.
3. Let s be the size of the loop. 
   Now we need 2 pointers again. The first pointer points at the head. Second 
   pointer should be s nodes ahead.
   Moves both pointers ahead step by step at same rate. This time the meeting 
   point will be the junction node.
*/
void removeLoop(node *head)
{
    // finding if loop exists or not
    node *slow = head, *fast = head;
    while (fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
        if (fast == slow)
            break;
    }
    if (fast == nullptr || fast->next == nullptr)
        return;

    // finding size of loop
    int loop = 1;
    while (slow->next != fast)
    {
        loop++;
        slow = slow->next;
    }

    // moving fast pointer 'loop' nodes ahead
    slow = head, fast = head;
    while (loop--)
        fast = fast->next;

    // now move each pointer 1 node each, when they meet thats the meeting point
    while (slow != fast)
    {
        slow = slow->next;
        fast = fast->next;
    }

    // get the slow pointer to the end of linked list
    while (slow->next != fast)
        slow = slow->next;

    // now slow points to last node, so make its next node nullptr
    slow->next = nullptr;
}

int main(int argc, char const *argv[])
{
    LinkedList ll;
    node *head;
    int arr1[] = {3, 6, 9, 15, 30};
    head = ll.loadList(arr1, 5);
    head->next->next->next->next->next = head;

    removeLoop(head);

    while (head)
    {
        cout << head->val << "  ";
        head = head->next;
    }
    cout << endl;

    return 0;
}
