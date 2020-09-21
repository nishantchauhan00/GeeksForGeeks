int countSubs(Node *root, int x){
    if (!root)
	    return 0;
	    
	int counts = countSubs(root->left, x) + countSubs(root->right, x);
	
	if (root->left)
	    root->data += root->left->data;
	if (root->right)
	    root->data += root->right->data;
	 
	if (root->data == x)
	    return counts + 1;
	else
	    return counts;
}

int countSubtreesWithSumX(Node* root, int X)
	return countSubs(root, X);


/*
Input:
       5
    /    \
  -10     3
 /   \   /  \
 9   8 -4    7
X = 7
Output: 2
Explanation: Subtrees with sum 7 are
[9, 8, -10] and [7] (refer the example
in the problem description).
*/

/*
5
 \
  4
    \
      1
[1], [4, 1] and [5, 4, 1] are subtrees, not [5] or [5, 4]


this is a subtree
    5
 /    \
10     3


this is also a subtree
    5


subtree starts from bottom, so it cant be in middle or top
*/