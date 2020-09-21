#include <queue>
#include "../utils/BinaryTree.hpp"
using namespace std;

void checkChilds(TreeNode *head, int &n, queue<TreeNode *> &qu)
{
    if (head->left)
    {
        ++n;
        qu.push(head->left);
    }
    if (head->right)
    {
        ++n;
        qu.push(head->right);
    }
}

void connect(TreeNode *p)
{
    queue<TreeNode *> qu;
    qu.push(p);
    int n = 1;
    while (!qu.empty())
    {
        TreeNode *temp = qu.front(), *temp2 = NULL;
        qu.pop();
        int n1 = 0;
        checkChilds(temp, n1, qu);
        for (int i = 1; i < n; i++)
        {
            temp2 = qu.front();
            qu.pop();
            checkChilds(temp2, n1, qu);
            temp->nextRight = temp2;
            temp = temp2;
        }
        temp->nextRight = NULL;
        n = n1;
    }
}
