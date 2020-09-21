# gives tle
def maxRectangle1(M, row, col):
    mheight = [[0 for i in range(col)] for j in range(row + 1)]
    leftbound = [[0 for i in range(col)] for j in range(row + 1)]
    rightbound = [[(col - 1) for i in range(col)] for j in range(row + 1)]

    for r in range(1, row + 1):
        lb = 0  # to maintain left border
        # filling mheight and mleft as they both are to filled from left to right
        for c in range(col):
            if M[r - 1][c] == 1:
                mheight[r][c] = mheight[r - 1][c] + 1
                # left-bound for position (row, col) will be maximum of
                # lb or upper value, because if there is a rectangle taller
                # than the lb, we have to use that because taller rectangle
                # could have left bound farther to right. we have to be
                # conservative/restrictive by taking rigthmost leftbound.
                leftbound[r][c] = max(lb, leftbound[r - 1][c])
            else:
                # mheight[r][c] = 0
                # leftbound[r][c] = 0
                lb = c + 1

        rb = col - 1
        # we have to do similar for rightbound but in opposite direction
        for c in range(col - 1, -1, -1):
            if M[r - 1][c] == 1:
                rightbound[r][c] = min(rb, rightbound[r - 1][c])
            else:
                # rightbound[r][c] = col - 1
                rb = c - 1

    # finding maximum area
    max_area = 0
    for r in range(1, row + 1):
        for c in range(col):
            # width = right - left
            # so, current_area = (right - left)*height
            if M[r - 1][c] == 1:
                max_area = max(
                    max_area, (rightbound[r][c] - leftbound[r][c] + 1) * mheight[r][c]
                )

    return max_area


"""
Idea is to use DP
Check with every row and if above is 1 then add above row's dp value to 
current row.
Finally we will have an histogram.

Use Algo to find Max Area in Histogram for every row
"""
def maxRectangle(M, row, col):
    def maxHistogramArea(histogram):
        stack, i = [], 0
        max_area = 0

        while i < len(histogram):
            # if stack empty or last value on stack is lower than current
            # value, then push index
            if len(stack) == 0 or histogram[stack[-1]] <= histogram[i]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                # Calculate the area with histogram[top] stack as smallest bar
                if len(stack) == 0: # stack empty
                    # if stack is empty that means it is smallest value uptill
                    # current index 'i'
                    # curr_area = height*(left - right)
                    curr_area = histogram[top]*(i - 0)
                else:
                    curr_area = histogram[top] * (i - stack[-1] - 1)
                max_area = max(max_area, curr_area)

        while stack:
            top = stack.pop()
            # Calculate the area with histogram[top] stack as smallest bar
            if len(stack) == 0: # stack empty
                # if stack is empty that means it is smallest value uptill
                # current index 'i'
                # curr_area = height*(left - right)
                curr_area = histogram[top]*(i - 0)
            else:
                curr_area = histogram[top] * (i - stack[-1] - 1)
            max_area = max(max_area, curr_area)
        
        return max_area
    
    # max rectangle in binary algorithm
    rect_max_area = 0
    mheight = [0]*(col+1)
    for r in range(1, row + 1):
        for c in range(col):
            mheight[c] = (mheight[c] + 1) if (M[r - 1][c] == 1) else 0
    
        rect_max_area = max(rect_max_area, maxHistogramArea(mheight))

    return rect_max_area


'''
smaller histogram solution

stack = [-1]
for i in xrange(n + 1):
    while height[i] < height[stack[-1]]:
        h = height[stack.pop()]
        w = i - 1 - stack[-1]
        ans = max(ans, h * w)
    stack.append(i)

we have to append an extra 0 height histogram(means just a zero) at the end
of histogram array, so that we dont have to run another extra while loop to
ensure that stack is empty
OR
We loop from 0 -> n+1 because we are considering a height array with a zero at 
the end. We add a zero at the end because we want to always ensure a condition 
in which the current considered height is less than the height's stored in the 
stack.

stack will never b
'''

