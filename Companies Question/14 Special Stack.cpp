#include <iostream>
#include <stdlib.h>
#include <stack>

using namespace std;

// to get minimum of stack just change push operation and always
// push keep smallest element on top of stack 
// or
// is you have to maintain order use hashmap for minimum element OR
// maintain another min stack,
// but it will take more time and memory


/*Complete the function(s) below*/
void push(int a);
bool isFull(int n);
bool isEmpty();
int pop();
int getMin();

stack<int> s;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, a;
        cin >> n;
        while (!isEmpty())
        {
            pop();
        }
        while (!isFull(n))
        {
            cin >> a;
            push(a);
        }
        cout << getMin() << endl;
    }
    return 0;
}


/*Complete the function(s) below*/
void push(int a)
{
    if (isEmpty() || s.top() >= a)
        s.push(a);
    else
    {
        int el = s.top();
        s.pop();
        s.push(a);
        s.push(el);
    }
}

bool isFull(int n)
{
    return s.size() == n;
}

bool isEmpty()
{
    return s.empty();
}

int pop()
{
    int el = s.top();
    s.pop();
    return el;
}

int getMin()
{
    return s.top();
}
