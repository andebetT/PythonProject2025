#you  are given an integer array arr[] for every element in the array your task is to find the previous smaller element
def previous_smaller_element(arr):
    n = len(arr)
    result = [-1] * n  # Initialize result with -1
    stack = []  # Stack to keep track of indices

    for i in range(n):
        # Pop elements from the stack while the current element is smaller or equal
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        # If stack is not empty, the top of the stack is the previous smaller element
        if stack:
            result[i] = arr[stack[-1]]
        # Push the current index onto the stack
        stack.append(i)

    return result

# Test cases
arr = [3, 2, 1, 4]
arr1 = [1, 6, 2]
print(previous_smaller_element(arr))   # Output: [-1, -1, -1, 1]
print(previous_smaller_element(arr1))  # Output: [-1, 1, 1]



def previous_greater_element(arr):
    n = len(arr)
    result = [-1] * n  # Initialize result with -1 for no greater element
    stack = []  # Stack to keep track of indices

    for i in range(n):
        # Pop elements from the stack while the current element is greater or equal
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        # If the stack is not empty, the top of the stack is the previous greater element
        if stack:
            result[i] = arr[stack[-1]]
        # Push the current index onto the stack
        stack.append(i)

    return result

# Test case
arr = [3, 2, 1, 4]
print(previous_greater_element(arr))  # Output: [ -1, 3, 2, -1 ]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    if not root:
        return targetSum == 0

    targetSum -= root.val

    if not root.left and not root.right:  # It's a leaf node
        return targetSum == 0

    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)

