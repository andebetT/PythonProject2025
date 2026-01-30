from operator import index


def count_alive_fishes(A, B):
    stack = []

    for i in range(len(A)):
        while B[i] == 'L' and stack and B[stack[-1]] == 'R':
            right_fish_index = stack.pop()
            if A[right_fish_index] > A[i]:
                stack.append(right_fish_index)
                break
            elif A[right_fish_index] < A[i]:
                stack.append(i) # The left fish survives
                break
            else:
                break  # Both fishes die
        else:
            stack.append(i)

    return len(stack)

#TC-o(n)
#SC-O(N)
# Example Usage
sizes = [4, 3, 2, 1, 5]
directions = "RRRRL"
print(count_alive_fishes(sizes, directions))  # Output: 2


def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

# Example Usage
string_a = "abcabcbb"
print(length_of_longest_substring(string_a))  # Output: 3


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root: TreeNode) -> bool:
    if not root:
        return True  # An empty tree is symmetric

    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True  # Both nodes are None, hence symmetric
        if not t1 or not t2:
            return False  # One node is None, the other is not

        # Check values and subtrees
        return (t1.val == t2.val and
                is_mirror(t1.left, t2.right) and
                is_mirror(t1.right, t2.left))

    return is_mirror(root.left, root.right)

# Example Usage
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(3)
root.right.right = TreeNode(1)

print(is_symmetric(root))  # Output: True

from collections import deque


def max_in_subarrays(arr, B):
    if not arr or B <= 0:
        return []

    n = len(arr)
    if B > n:
        return []

    result = []
    dq = deque()

    for i in range(n):
        # Remove indices that are out of the bounds of the window
        if dq and dq[0] < i - B + 1:
            dq.popleft()

        # Remove indices from the back while the current element is greater
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        # Add current index to the deque
        dq.append(i)

        # Start adding results after the first B elements
        if i >= B - 1:
            result.append(arr[dq[0]])

    return result


# Example usage
arr = [1, 3, -1, -3, 5, 3, 6, 7]
B = 3
print(max_in_subarrays(arr, B))  # Output: [3, 3, 5, 5, 6, 7]



from collections import deque


def min_in_subarrays(arr, B):
    print(arr)
    if not arr or B <= 0:
        return []

    n = len(arr)
    if B > n:
        return []

    result = []
    dq = deque()

    for i in range(n):
        # Remove indices that are out of the bounds of the window
        if dq and dq[0] < i - B + 1:
            dq.popleft()

        # Remove indices from the back while the current element is greater
        while dq and arr[dq[-1]] > arr[i]:
            dq.pop()

        # Add current index to the deque
        dq.append(i)

        # Start adding results after the first B elements
        if i >= B - 1:
            result.append(arr[dq[0]])

    return result


# Example usage
arr = [1, 3, -1, -3, 5, 3, 6, 7]
B = 3
print(min_in_subarrays(arr, B))  # Output:

import bisect
def find_peak_element(arr):
    left=0
    right=len(arr)-1
    while left<right:
        mid=(left+right)//2
        if arr[mid]<arr[mid+1]:
            left=mid+1
        elif arr[mid]>arr[mid+1]:
            right=mid
        else:
            endex=bisect.bisect_left(arr,arr[mid])
            print(endex)
            return arr[endex]
    return arr[left]
print(find_peak_element([1,2,3,20,20,20,4]))


import math
def find_duplicate(nums):
    for num in nums:
        value=math.fabs(num)
        if nums[value-1]>0:
            nums[value-1]=-nums[value-1]
        else:
            return value
    return -1



arr=[1,2,3,4,2,2]
print(find_peak_element(arr))


def print_hash_tag(n):
    for i in range(n):
        out_pur=""
        for j in range(n):
            if (i+j)%2==0:
                out_pur+=" #"
            else:
                out_pur+=" *"
        print(out_pur)
print(print_hash_tag(4))


def find_log(n):
    if n<=1:
        return 0
    return 1+find_log(n//2)
print(find_log(8))

