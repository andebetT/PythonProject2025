def min_removals_for_non_decreasing(arr):
    n = len(arr)
    # Count elements that can stay in a non-decreasing arrangement
    count = 0
    # Start from the end and track the current maximum allowed value
    current_max = float('inf')
    for num in reversed(arr):
        if num <= current_max:
            count += 1
            current_max = num

    # The minimum removals would be the total elements minus the elements in a valid non-decreasing order
    return n - count

# Example usage
arr1_1 = [2, 1, 3, 2, 1]
arr1_2 = [1, 3, 2, 1, 3, 3]
arr1_3 = [2, 2, 2, 2, 3, 3]

print(min_removals_for_non_decreasing(arr1_1))  # Output: 3
print(min_removals_for_non_decreasing(arr1_2))  # Output: 2
print(min_removals_for_non_decreasing(arr1_3))  # Output: 0

from collections import Counter


def minLength(s):
        # Count the frequency of each character in the string
    freq = Counter(s)

        # The minimum length of `t` can be obtained by counting unique characters
    return sum(count // 2 + count % 2 for count in freq.values())


# Example usage
input_string1 = "abba"
input_string2 = "cdef"

print("Minimum length for input 'abba':", minLength(input_string1))
print("Minimum length for input 'cdef':", minLength(input_string2))