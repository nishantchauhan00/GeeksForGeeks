void helper1(Node *root, int k, int &diff)
{
    if (!root)
        return;

    diff = min(diff, abs(root->data - k));
    helper1(root->left, k, diff);
    helper1(root->right, k, diff);
}

void helper(Node *root, int k, int &diff)
{
    if (!root)
        return;
    else if (root->data == k)
    {
        diff = 0;
        return;
    }
    else
    {
        diff = min(diff, abs(root->data - k));
        if (k < root->data)
            helper(root->left, k, diff);
        else // (k > root->data)
            helper(root->right, k, diff);
    }
}

int minDiff(Node *root, int k)
{
    int diff = INT_MAX;
    helper(root, k, diff);
    return diff;
}
