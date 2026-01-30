def sum_of_list(arr, start, end):
    if start >= end:  # Base case: no elements to sum
        return 0
    return arr[start] + sum_of_list(arr, start + 1, end)

arr = [1, 2, 3, 4, 5]
print(sum_of_list(arr, 0, len(arr)))  # Output: 15



def recursive_fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return recursive_fib(n-1)+recursive_fib(n-2)

print(recursive_fib(5))


#write a python program to print 1 to N without using any loops

def print_numbers(N):
    if N < 1:
        return
    print_numbers(N - 1)
    print(N)

# Call the function to print numbers from 1 to 6
print_numbers(6)


def revers_string(s):
    if s == "":  # Base case: if the string is empty, return it
        return s
    return s[-1] + revers_string(s[:-1])

# Example usage
result = revers_string("hello")
print(result)  # Output: "olleh"



#write a python program to find the product of two numbers using recursive function
def product_two_numbers(x,y):
    if x==0:
        return 0
    return y+product_two_numbers(x-1,y)
print(product_two_numbers(4,5))

#sum of digits of a number
def digit_sum(n):
    if n==0:
        return 0
    return n%10+digit_sum(n//10)

print(digit_sum(123))


#length of a given string
def length_of_string(s):
    if s=="":
        return 0
    return 1+length_of_string(s[1:])


s="andebet"
print(length_of_string(s))



def nCr(n, r):
    # Base case: if r is 0 or r equals n, return 1
    if r == 0 or r == n:
        return 1
    # Recursive case: nCr = (n-1)C(r-1) + (n-1)Cr
    return nCr(n - 1, r - 1) + nCr(n - 1, r)



#write n fibonaci series in reverse order

def fib_reverse(number):
    if number<=1:
        return number
    print(number)
    return fib_reverse(number-1)+fib_reverse(number-2)


print(fib_reverse(5))




a=[1,2,5]
b=a
print(a is b)
print(a==b)