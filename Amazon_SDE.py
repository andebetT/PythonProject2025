#reverse linked list using recursive
def reverse_linked_list(self,head):
        if not self.head or not head.next:
            return self.head
        new_node=self.reverse_linked_list(self.head.next)
        self.head.next.next=self.head
        self.head=None
        return new_node

#given an array of numbers and integer k rotate an array by k in right direction inspace


def reverse_array(nums,k):
    n=len(nums)
    k=k%n
    def swap_elements(left,right):
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
    swap_elements(0,n-1)
    swap_elements(0,k-1)
    swap_elements(k,n-1)
    return nums

arr=[1,2,3,4,5,6]
print(reverse_array(arr,3))



def gcd_of_two_numbers(a,b):
    while b!=0:
        a,b=b,a%b
    return a
print(gcd_of_two_numbers(2,8))



#non-overlapping intervals leet code 435

def erase_overlapping_intervals(intervals):
    intervals.sort()
    removal_count = 0
    previous_end = intervals[0][1]
    for interval in intervals[1:]:
        if interval[0] >= previous_end:

            previous_end = interval[1]
        else:
            removal_count += 1
            previous_end = min(previous_end, interval[1])
    return removal_count


#leetcode 452
def findMinArrowShots(points):
    points.sort()
    min_arrow = len(points)
    previous_end = points[0][1]
    for start, end in points[1:]:
        if start <= previous_end:
            min_arrow -= 1
            previous_end = min(previous_end, end)
        else:
            previous_end = end

    return min_arrow



def next_greater_element(nums):
    # Initialize the stack and the result array
    stack = []
    result = [-1] * len(nums)  # Default all elements to -1

    for i in range(len(nums)):
        # Process the elements in the stack
        while stack and nums[i] > nums[stack[-1]]:
            # Pop the index from the stack
            index = stack.pop()
            result[index] = nums[i]  # Update the result for that index

        # Push the current index onto the stack
        stack.append(i)

    return result

# Example usage
nums = [4, 5, 2, 10]
print(next_greater_element(nums))  # Output: [5, 10, 10, -1]



#number of rotations in rotated  sorted array
def number_of_rotation(arr):
    pos=0
    while pos<len(arr)-1:
        if arr[pos]<arr[pos+1]:
            pos+=1
        else:
            return pos+1
print(number_of_rotation([4,5,6,1,2,3]))


def findnumber(numbers):

    while len(numbers)>2:
        temp=[(numbers[i]+numbers[i+1])%10 for i in range(len(numbers)-1)]
        numbers=temp
    return str(numbers[0])+str(numbers[1])#f"{numbers[0]}{numbers[1]}"
numbers=[4,5,6,7]
print(findnumber(numbers))

import heapq
def getrelativerating(skill,rating,k):
    n=len(skill)
    arr=list(enumerate(zip(skill,rating)))
    arr.sort(key=lambda x:x[1][0])
    min_heap=[]
    result=[0]*n
    s=0
    for i in range(n):
        sk,ra=arr[i][1]
        index=arr[i][0]
        result[index]=s
        s+=ra
        heapq.heappush(min_heap,ra)
        if len(min_heap)>k:
            s-=heapq.heappop(min_heap)
    return result
skill=[1,2,3,4]
rating=[40,30,20,10]
k=2
print(getrelativerating(skill,rating,k))


def findmaximumchange(temperature):
    max_val=float("-inf")
    for i in range(len(temperature)):
        maximum_change=max(sum(temperature[:i+1]),sum(temperature[i:]))
        if maximum_change>max_val:
            max_val=maximum_change
    return max_val
temperature=[6,-2,5]
print(findmaximumchange(temperature))
# let us optimize the above code using prefix sum and postfix sum

def findmaximumchange(temperature):
    max_val=float("-inf")
    n=len(temperature)
    prefix_sum=[0]*n
    prefix_sum[0]=temperature[0]
    postfix_sum=[0]*n
    postfix_sum[-1]=temperature[-1]
    for i in range(1,len(temperature)):
        prefix_sum[i]+=prefix_sum[-1]+temperature[i]
    for i in range(n-2,-1,-1):
        postfix_sum[i]+=postfix_sum[i+1]+temperature[i]
    for i in range(n):
        max_val=max(max_val,max(postfix_sum[i],prefix_sum[i]))
    return max_val
temperature=[6,-2,5]
print(findmaximumchange(temperature))



#given an integer n count the total number of prime numbers strictly less than n

def count_prime(n):
    count = 0
    if n < 2:
        return 0

    prime = [True] * n
    prime[0] = prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n, i):  # Mark multiples of i
                prime[j] = False

    count = sum(1 for i in range(2, n) if prime[i])  # Counting primes in one line
    return count
print(count_prime(10))




#given an integer array nums,return the maximum possible sum of elements pf the array such that it is divisible by 3
#leetcode 1262

def maxSumDivThree(nums):
    total=sum(nums)
    if total%3==0:
        return total
    min_reminder1=float("inf")
    min_reminder2 = float("inf")
    #this are the minimum removed elements to make the sum is divisible by 3
    for n in nums:
        if n%3==1:
            min_reminder1=min(min_reminder1,n)
        elif n%3==2:
            min_reminder2=min(min_reminder2,n)
    if total%3==1:
        option1=min_reminder1
        option2=min_reminder2*2 if min_reminder2!=float("inf") else float("inf")
    else:
        option1=min_reminder2
        option2=min_reminder1*2 if min_reminder1!=float("inf") else float("inf")
    removed_element=max(option1,option2)
    return total-removed_element if removed_element!=float("inf") else 0
nums=[3,6,5,1,8]
print(maxSumDivThree(nums))


'''function isSymmetric(root):
    if root is null:
        return true
    return isMirror(root.left, root.right)

function isMirror(left, right):
    if left is null and right is null:
        return true
    if left is null or right is null:
        return false
    return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)'''

#length of longest sub string without repeating char
def length_of_longest_substring(s):
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
string_a = "AaaA"
print(length_of_longest_substring(string_a))  # Output: 3