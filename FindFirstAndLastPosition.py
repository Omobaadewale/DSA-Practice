#Challenge: Find the First and Last Position of an Element in a Sorted Array
# Problem Statement: Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If the target is not found in the array, return [-1, -1]

 

def searchRange(nums, target):
    newValue = []
    for index, value in enumerate(nums):
        if value == target:
            newValue.append(index)
    if newValue:     #checks if newvalue is not empty, if not empty return the first and last indices!!!
           return [newValue[0],newValue[-1]]
    else:
         return [-1,-1]

nums = [5,7,7,8,8,10]
target = 6
print(searchRange(nums,target))