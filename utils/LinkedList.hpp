#include <stdlib.h>
#include <iostream>
using namespace std;
#define LinkedList_H
struct node
{
    int val;
    node *next;
    node(int x) : val(x), next(NULL) {}
    node() {}
};

class LinkedList
{
public:
    void printList(node *head)
    {
        while (head != NULL)
        {
            cout << head->val << "  ";
            head = head->next;
        }
    }

    void printListReverse(node *head)
    {
        if (head != NULL)
        {
            printListReverse(head->next);
            cout << head->val << "  ";
        }
    }

    int countNodes(node *head)
    {
        int count = 0;
        while (head != NULL)
        {
            count++;
            head = head->next;
        }
        return count;
    }

    int minList(node *head)
    {
        int minel = INT_FAST32_MAX;
        while (head != NULL)
        {
            if (minel > head->val)
            {
                minel = head->val;
            }
            head = head->next;
        }
        return minel;
    }

    int maxList(node *head)
    {
        int maxel = INT_FAST32_MIN;
        while (head != NULL)
        {
            if (maxel < head->val)
            {
                maxel = head->val;
            }
            head = head->next;
        }
        return maxel;
    }

    int sumList(node *head)
    {
        int sum = 0;
        while (head != NULL)
        {
            sum += head->val;
            head = head->next;
        }
        return sum;
    }

    bool searchList(node *head, int searchEl)
    {
        while (head != NULL)
        {
            if (searchEl == head->val)
            {
                return true;
            }
            head = head->next;
        }
        return false;
        // Move to Head solution(will need to pass head after change)
        // node *follow;
        // node *first = head;
        // while(head!=NULL){
        //     if(searchEl == head->val){
        //         follow->next = head->next;
        //         head->next = first;
        //         return true;
        //     }
        //     follow = head;
        //     head = head->next;
        // }
        // return false;
    }

    node *insertList(node *head, int el, int pos = -1)
    {
        /**
         * For default pos = -1, it will insert at last.
         * returns pointer to head of list
        */
        node *insNode = new node(el);
        node *first = head;
        if (pos == -1)
        {
            if (head == NULL)
            {
                return insNode;
            }
            while (head->next != NULL)
            {
                head = head->next;
            }
            head->next = insNode;
            return first;
        }
        else
        {
            if (head == NULL)
            {
                return insNode;
            }
            else if (pos == 0)
            {
                insNode->next = head;
                return insNode;
            }
            else
            {
                for (int i = 0; i < pos - 1 && head->next != NULL; i++)
                {
                    head = head->next;
                }
                insNode->next = head->next;
                head->next = insNode;
                return first;
            }
        }
    }

    bool checkSorted(node *head, bool ascending = true)
    {
        node *follow;
        if (ascending)
        {
            while (head->next != NULL)
            {
                follow = head;
                head = head->next;
                if (head->val < follow->val)
                {
                    return false;
                }
            }
            return true;
        }
        else
            while (head->next != NULL)
            {
                follow = head;
                head = head->next;
                if (head->val > follow->val)
                {
                    return false;
                }
            }
        return true;
        {
            return true;
        }
    }

    node *mergeLists(node *head, node *head2, bool ascending = true)
    {
        /**
         * Implementation of decreasing order lists is left
        */
        node *first = head, *second = head2, *third, *last;
        // third points to head of the merged list
        if (head->val < head2->val)
        {
            last = third = first;
            first = first->next;
            last->next = NULL;
        }
        else
        {
            last = third = second;
            second = second->next;
            last->next = NULL;
        }
        while (first != NULL && second != NULL)
        {
            if (first->val > second->val)
            {
                last->next = second;
                last = second;
                second = second->next;
                last->next = NULL;
            }
            else
            {
                last->next = first;
                last = first;
                first = first->next;
                last->next = NULL;
            }
        }
        // For remaining elements
        if (first != NULL)
        {
            last->next = first;
        }
        if (second != NULL)
        {
            last->next = second;
        }
        return third;
    }

    node *insertSortedList(node *head, int el, bool ascending = true)
    {
        node *insNode = new node(el);
        node *follow;
        if (head == NULL)
        {
            return insNode;
        }
        if (ascending)
        {

            if ((head->val) > el)
            {
                insNode->next = head;
                return insNode;
            }
            node *first = head;
            while (head != NULL && (head->val) < el)
            {
                follow = head;
                head = head->next;
            }
            insNode->next = follow->next;
            follow->next = insNode;
            return first;
        }
        else
        {
            if (head->val < el)
            {
                insNode->next = head;
                return insNode;
            }
            node *first = head;
            while (head != NULL && head->val > el)
            {
                follow = head;
                head = head->next;
            }
            insNode->next = head;
            follow->next = insNode;
            return first;
        }
    }

    node *loadList(int *arr, int n)
    {
        // returns pointer to head of list
        if (n < 1)
        {
            return nullptr;
        }
        node *first = new node(arr[0]);
        node *last = first;
        for (int i = 1; i < n; i++)
        {
            node *second = new node(arr[i]);
            last->next = second;
            last = last->next;
        }
        return first;
    }

    node *deleteNode(node *head, int pos = -1)
    {
        /*
        * Default: pos = -1 deletes last node
        */
        node *first = head;
        if (pos == 0 || pos < -1)
        {
            head = head->next;
            delete first;
            return head;
        }
        else if (pos == -1)
        {
            node *follow;
            while (head->next != NULL)
            {
                follow = head;
                head = head->next;
            }
            follow->next = NULL;
            delete head;
            return first;
        }
        else
        {
            node *follow;
            for (int i = 0; i < pos && head; i++)
            {
                follow = head;
                head = head->next;
            }
            if (head != NULL)
            {
                follow->next = head->next;
                delete head;
            }
            return first;
        }
    }

    node *removeDuplicates(node *head)
    {
        /**
         * Convert the list to set, i.e., no two nodes have equal values.
        */
        if (head->next == NULL || head == NULL)
        {
            return head;
        }
        else
        {
            node *first = head;
            node *follow = head;
            head = head->next;
            while (head != NULL)
            {
                if (head->val == follow->val)
                {
                    follow->next = head->next;
                    delete head;
                    head = follow->next;
                }
                else
                {
                    follow = head;
                    head = head->next;
                }
            }
            return first;
        }
    }
    node *concatenateList(node *head, node *head2)
    {
        node *first = head;
        while (head->next != NULL)
        {
            head = head->next;
        }
        head->next = head2;
        return first;
    }
    node *reverseList(node *head)
    {
        node *follow = NULL;
        node *follow2 = NULL;
        while (head != NULL)
        {
            follow2 = follow;
            follow = head;
            head = head->next;
            follow->next = follow2;
        }
        return follow;
    }

    bool detectCycle(node *head)
    {
        /**
         * Floyd’s Cycle Finding Algorithm
         * returns true if loop present
        */
        node *slow = head;
        node *fast = head;
        while (slow != NULL && fast != NULL && fast->next != NULL)
        {
            //    move before check(is=f not, then on first check they output true)
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast)
            {
                return true;
            }
        }
        return false;
    }
};