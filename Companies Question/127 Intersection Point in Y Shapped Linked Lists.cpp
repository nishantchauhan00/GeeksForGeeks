#include <iostream>
#include <stdlib.h>
#include <unordered_set>
#include <stack>
#include "../utils/LinkedList.hpp"
#define INT_MIN -999999
using namespace std;


// 0.16s
int intersectPoint1(node *head1, node *head2)
{
    unordered_set<node *> hset;
    while (head2)
    {
        hset.insert(head2);
        head2 = head2->next;
    }

    while (head1)
    {
        if (hset.find(head1) != hset.end())
            return head1->val;
        head1 = head1->next;
    }

    return -1;
}

// 0.08s
int intersectPoint(node *head1, node *head2)
{
    stack<node *> st1, st2;
    while (head1)
    {
        st1.push(head1);
        head1 = head1->next;
    }

    while (head2)
    {
        st2.push(head2);
        head2 = head2->next;
    }

    int prev = -1;
    while (st1.top() == st2.top())
    {
        prev = st1.top()->val;
        st1.pop();
        st2.pop();
    }

    return prev;
}

// this solution takes advantage of given constraint that it will only have
// values >= 0
// 0.07s, O(1) space and O(n) time
int intersectPoint(node *head1, node *head2)
{
    while (head1)
    {
        if (head1->val == 0)
            head1->val = INT_MIN;
        else
            head1->val *= -1;
        head1 = head1->next;
    }

    while (head2)
    {
        if (head2->val == INT_MIN)
            return 0;
        else if (head2->val < 0)
            return (head2->val * -1);
        head2 = head2->next;
    }

    return -1;
}

int main(int argc, char const *argv[])
{
    LinkedList ll;
    node *head1, *head2;
    int arr1[] = {3, 6, 9, 15, 30};
    int arr2[] = {10};
    head1 = ll.loadList(arr1, 5);
    head2 = ll.loadList(arr2, 1);
    head2->next = head1->next->next->next;

    int intersection_val = intersectPoint(head1, head2);

    cout << intersection_val << endl;

    return 0;
}
