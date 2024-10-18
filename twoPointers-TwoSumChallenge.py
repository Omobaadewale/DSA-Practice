
#Day 1: Two Pointers
#Problem Statement: Pair Sum
#Objective: Given a sorted array of integers, find two numbers that add up to a specific target number.

def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]

#For some weird reason i understood the brute force approach better

def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sums == nums[i] + nums[j]
            if sums == target:
                return [i, j]
