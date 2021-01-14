from array import *

"""
n = int(input("How many numbers do you want in array :"))
arr = 
"""

arr = input("Enter the numbers:")   # takes the whole line of n numbers
sum = 0         
nums = array("i", map(int, arr.split(' '))) #l = list(map(int,arr.split(' '))) # split those numbers with space
for x in nums:
    sum = sum + x

print("Sum of all the elements is : ", sum)

