//User function Template for Java
/*class Node
{
    int data;
    Node left, right;
    
    Node(int data)
    {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}*/

// we have to take care if previous node was chosen or not
// now we have to take care of each case generated by chosing particular
// node or not
class GFG {
    int maxSum(Node head, boolean prevchosen) {
        if (head == null)
            return 0;
            
        if (prevchosen) {
            // if previous was chosen current node can't be taken into
            // account, so we take its left and right node into account
            // And for next call, prevchosen will become false
            int s1 = maxSum(head.left, false);
            int s2 = maxSum(head.right, false);
            return s1 + s2;
        } else {
            // if previous node was not chosen, then we can take current node
            // into account. But now its up to us if want to take current
            // node into account or not, therefore we will run both conditions
            // for both next left - right nodes, so total of four conditions

            // 1. Taking current node into account, means prevchosen = true
            int s1 = maxSum(head.left, true);
            int s2 = maxSum(head.right, true);
            int result1 = head.data + s1 + s2;
            // 2. Taking current node not into account
            int s3 = maxSum(head.left, false);
            int s4 = maxSum(head.right, false);
            int result2 = s3 + s4; // current node data won't be added here

            return Math.max(result1, result2);
        }
    }

    int getMaxSum(Node root) {
        return maxSum(root, false);
    }
}