#include <iostream>
#include <stdlib.h>
#include <vector>
#include <stack>
#include "../utils/BinaryTree.hpp"

using namespace std;


void pathPrintHelper(TreeNode *head, string vec)
{
    if(head==NULL) return;

    vec += to_string(head->data) + " ";
    if (!head->left && !head->right)
    {
        cout<<vec<<"#";
    }
    else{
        pathPrintHelper(head->left, vec);
        pathPrintHelper(head->right, vec);
    }
}

/* The function should print all the paths from root
to leaf nodes of the binary tree */
void printPaths(TreeNode *root)
{
    string s = "";
    pathPrintHelper(root, s);
    cout<<endl;
}

int main(int argc, char const *argv[])
{
    BinaryTree bt;
    int arr[] = {1, 2, 3, 4, 5, 6, 7};

    TreeNode *root;
    root = bt.createBinaryTree(arr, root, 0, 7);

    printPaths(root);

    return 0;
}
