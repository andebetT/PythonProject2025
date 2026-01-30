from collections import Counter
import heapq
from symtable import Class
def reorganizing_string(s):
    counter=Counter(s)
    if max(counter.values())>len(s)//2:
        return ""
    max_heap=[(-count,key) for key,count in counter.items()]
    heapq.heapify(max_heap)
    previous_char=''
    previous_count=0
    result=[]
    while max_heap:
        count,char=heapq.heappop(max_heap)
        result.append(char)
        if previous_count<0:
            heapq.heappush(max_heap,(previous_count,previous_char))
        previous_count=count+1
        previous_char=char
    return "".join(result) if len(result)==len(s) else ""
#nlogK-TC where k is the number of unique characters
#n SC to store the result of all given characters


s="aaabbnde"

print(reorganizing_string(s))

#this brute force
def maximum_right_element(arr):

    for i in range(len(arr)):
        max_val=arr[i]
        for j in range(i+1,len(arr)):
            if arr[j]>max_val:
                max_val=arr[j]
        if max_val>arr[i]:
            arr[i]=max_val
        else:
            arr[i]=-1
    return arr
a=[8,9,5,11,6,1,7,6]
print(maximum_right_element(a))


#input=[8,9,5,11,6,1,7,6]
#output=[11,11,11,-1,7,7,-1,-1]

def next_max_element(arr):
    maximum_right=arr[-1]
    arr[-1]=-1
    for i in range(len(arr) - 2, -1, -1):
        if maximum_right>arr[i]:
            arr[i]=maximum_right
        else:
            maximum_right=arr[i]
            arr[i]=-1


    return arr

a = [8, 9, 5, 11, 6, 1, 7, 6]
print(next_max_element(a))



#search suggestion system leet code 1268

def suggested_products(products,searchword):
    products.sort()
    result=[]
    left=0
    right=len(products)-1
    for i in range(len(searchword)):
        search=searchword[i]

        while left<=right and len(products[left])<=i or search!=products[left][i]:
            left+=1
        while left<=right and len((products[right]))<=i or search!=products[right][i]:
            right-=1
        words_left=right-left+1
        if words_left>=3:
            result.append([products[left],products[left+1],products[left+2]])
        elif words_left==2:
            result.append([products[left], products[left + 1]])
        elif words_left==1:
            result.append([products[left]])
        else:
            result.append([])

    return result
products=["mobile","mouse","moneypot","monitor","mousepad"]
searchword="mouse"

print(suggested_products(products, searchword))


class Rectangle:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)

    def POP(self):

        self.stack.pop()
    def isempty(self):
        return len(self.stack)==0

    def top(self):
        if self.stack:
            return self.stack[-1]
rectangle=Rectangle()
rectangle.push(10)
rectangle.POP()
print(rectangle.isempty())
print(rectangle.top())




def power(base,val):
    result=base
    count=0
    while result<=val:
        result=result*2
        count+=1
        if result==val:
            return count


print(power(2,512))



def print_val(array, start, end):
    if start<=end:
        print(array[start])
        print_val(array, start + 1, end)
    return
arr=[1,2,3,4,5]
print(print_val(arr,0,len(arr)-1))


#find the left most index of a target

def left_most(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        middle=(left+right)//2
        if arr[middle]<target:
            left=middle+1
        else:
            right=middle-1
    return left


array=[1,2,3,3,3,4,5]
target=3
print(left_most(array,target))


#find the right most index of a target

def right_most(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        middle=(left+right)//2
        if arr[middle]<=target:
            left=middle+1
        else:
            right=middle-1
    return right


array=[1,2,3,3,3,4,5]
target=3
print(right_most(array,target))




def sliding_window(arr):
    left=0
    maxl=0
    maxr=0
    maxsum=arr[0]
    l=0
    currentsum=0
    for r in range(len(arr)):
        if currentsum<0:
            currentsum=0
            l=r
        currentsum+=arr[r]
        if currentsum>maxsum:
            maxsum=currentsum
            maxl,maxr=l,r
    return [maxl,maxr]
arr=[4,10,-15,1,6]
print(sliding_window(arr))
