
#Problem Statement: Remove Duplicates from Sorted Array

#Objective: Given a sorted array, remove the duplicates in-place such that each element appears only once and return the new length.
#Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.


# Sample solution
def remove_duplicates(nums):
    if not nums:
        return 0

    write_index = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[write_index] = nums[i]
            write_index += 1

    return write_index

# Example usage
nums = [1, 1, 2]
length = remove_duplicates(nums)
print(length)  # Output: 2
print(nums[:length])  # Output: [1, 2]

# using brute force approach
def remove_duplicates(arr):
    return [x for i, x in enumerate(arr) if x not in arr[:i]]

arr = [1,1,2]
print(remove_duplicates(arr))  # Output: [1, 2]

# my own solution
def rem_dup(arr):
    # new dictionary to store the value and index
    new_dict = {}
    #looping through the array and checking each value
    for i in arr:
        # checks if i not in the dictionary : then next line sets the first i at index 1
        if i not in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1
            # returns the value for the selected key in the dictionary
    return list(new_dict.keys()) # Output: [1, 2]       
    #return(new_dict.keys()) #output: dict_keys([1, 2]) 


arr = [1,1,2]
print(rem_dup(arr))