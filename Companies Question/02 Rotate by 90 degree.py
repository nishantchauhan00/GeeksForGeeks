# arr = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

def rotate():
    rows = len(arr) - 1
    cols = len(arr[0]) - 1

    def helper(i, j, n):
        tl = arr[i + j][i]
        tr = arr[i][cols - i - j]
        dl = arr[rows - i][i + j]
        dr = arr[rows - i - j][cols - i]

        arr[i + j][i] = tr
        arr[i][cols - i - j] = dr
        arr[rows - i][i + j] = tl
        arr[rows - i - j][cols - i] = dl
    
    for i in range(int(len(arr)/2)):
        n = len(arr[0]) - 2*i - 1
        for j in range(n):
            helper(i, j, n)

'''
Another way to solve this is reverse every row of the matrix and then take its 
transpose.

1 2 3 | -> | 3 2 1 | -> | 3 6 9
4 5 6 | -> | 6 5 4 | -> | 2 5 8
7 8 9 | -> | 9 8 7 | -> | 1 4 7

void rotate(vector<vector<int> >& matrix)
{
int n = (int) matrix.size();
int m = (int) matrix[0].size();
for(int i = 0; i < n; i++){

reverse(matrix[i].begin(), matrix[i].end());
}
for(int i = 0; i < n; i++){
for(int j = i; j < m; j++){
swap(matrix[i][j], matrix[j][i]);
}

}
}
'''



rotate()

for e in arr:
    for el in e:
        print("{:2d} ".format(el), end=" ")
    print()

