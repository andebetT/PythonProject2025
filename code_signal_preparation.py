from inspect import stack


#given a string return true if it is palindrome after rearranging else return false


def palindromeRearranging(s):
    dictionary={}
    for char in s:
        if char in dictionary:
            dictionary[char]+=1
        else:
            dictionary[char]=1
    odd_count=0
    for key,val in dictionary.items():
        if val%2==1:
            odd_count+=1
    return odd_count<=1

s="aabb"
print(palindromeRearranging(s))



#two arrays are called similar if one can be obtained from another by swapping at most one pair of elements
#example arr1=[1,2,3],array2=[1,2,3] they are equal no need of swap
#example arr1=[1,2,3],arr2=[2,1,3] we can make equal after swapping [2,1] t0[1,2]
def areSimilar(arr1,arr2):
    if "".join(map(str,arr1))=="".join(map(str,arr2)):
        return True
    array1=[]
    array2=[]
    for i in range(len(arr1)):
        if arr1[i]!=arr2[i]:
            array1.append(arr1[i])
            array2.append((arr2[i]))
    array2.reverse()
    return array2==array1
arr1=[1,2,3]
arr2=[2,1,3]
print(areSimilar(arr1, arr2))



#given a sequence of integers as an array determine whether is it possible to obtain strictly increasing sequence by removing no more than one element from the array
def almostIncreasingSequence(sequence):
    non_increasing_count=0
    for i in range(1,len(sequence)):
        if sequence[i]<=sequence[i-1]:
            non_increasing_count+=1
    return non_increasing_count<=1
sequance1=[1,3,2,1]
sequance2=[1,3,2]
print(almostIncreasingSequence(sequance1))
print(almostIncreasingSequence(sequance2))


#write a function that reverse characters in (possibly nested) parentheses in the input string
#example "(bar)"="rab"
#example "foo(bar)baz"="foorabbaz"
def reverseInParenthesis(inputString):
    stack=[]
    for char in inputString:
        if char!=")":
            stack.append(char)
        else:
            temp_stack=[]
            while stack[-1]!="(":
                temp_stack.append(stack.pop())
            stack.pop()
            stack.extend(temp_stack)
            temp_stack=[]
    return "".join(stack)
inputString="foo(bar)baz"
print(reverseInParenthesis(inputString))


#you are given an array of integers representing coordinate of obstacles situated on a straight line.
#assume that you are jumping from the point with coordinate 0 to the right.you are allowed only to make jumps of the same length represented by some integer
#find the minimal length of the jump enough to avoid all of the obstacles.
def avoidObstacles(inputArray):
    min_jump_length=1
    while True:
        can_jump=True
        for obstacles in inputArray:
            if obstacles%min_jump_length==0:# that means we are at obstacles so we need to try other
                can_jump=False
                break
        if can_jump:
            return min_jump_length
        min_jump_length+=1
    return min_jump_length
inputArray=[5,3,6,7,9]
print(avoidObstacles(inputArray))


def add_border(picture):
    # Create the border
    border = '*' * (len(picture[0]) + 2)

    # Initialize the new picture with the top border
    bordered_picture = [border]

    # Add asterisk border to each row
    for row in picture:
        bordered_picture.append('*' + row + '*')

    # Add the bottom border
    bordered_picture.append(border)

    return bordered_picture


# Example usage
picture = ["abc", "ded"]
print(add_border(picture))


def arrayChange(inputArray):
    moves = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] <= inputArray[i - 1]:
            # Calculate the moves needed
            required_value = inputArray[i - 1] + 1
            moves += required_value - inputArray[i]
            inputArray[i] = required_value  # Update to the new required value
    return moves


def isIPv4Address(inputString):
    parts = inputString.split('.')

    # Check if there are exactly four parts
    if len(parts) != 4:
        return False

    for part in parts:
        # Check if the part is a valid number and in the correct range
        if not part.isdigit() or not (0 <= int(part) <= 255):
            return False
        # Check for leading zeros
        if len(part) > 1 and part[0] == '0':
            return False

    return True
n=6
for i in range(n):
    if i==0 or i==n-1:
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")





