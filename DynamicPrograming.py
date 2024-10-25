# Problem Statement: Longest Increasing Subsequence (LIS)
# Objective: Given an array of integers, find the length of the longest increasing subsequence.

# Description:

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
# An increasing subsequence is a subsequence where each element is greater than the previous one.

# Constraints:

# The length of the array will be between 1 and 2500.
# The elements of the array will be between -10^4 and 10^4.
# Approach
# Dynamic Programming:
# Use a dynamic programming array dp where dp[i] represents the length of the longest increasing subsequence that ends with arr[i].
# Initialize dp with 1s because the minimum length of the increasing subsequence ending at each element is 1 (the element itself).
# For each element arr[i], check all previous elements arr[j] (where j < i). If arr[j] < arr[i], update dp[i] as dp[i] = max(dp[i], dp[j] + 1).
# Result:
# The length of the longest increasing subsequence will be the maximum value in the dp array.

def length_of_lis(arr):
    if not arr:
        return 0

    dp = [1] * len(arr)

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Test the function
arr = [10, 9, 2, 5, 3, 7, 101, 18]
print(length_of_lis(arr))  # Output: 4


##############################################################################################################################################


# Problem Statement: 0/1 Knapsack Problem
# Objective: Imagine you have a backpack with a weight limit, and you want to pack it with items that have both weights and values.
# Your goal is to maximize the total value of the items in your backpack without exceeding the weight limit.

def knapsack(weights, values, max_weight):
    num_items = len(weights)
    value_table = [[0 for _ in range(max_weight + 1)] for _ in range(num_items + 1)]

    for item in range(1, num_items + 1):
        for weight in range(1, max_weight + 1):
            if weights[item - 1] <= weight:
                value_table[item][weight] = max(
                    value_table[item - 1][weight],
                    value_table[item - 1][weight - weights[item - 1]] + values[item - 1]
                )
            else:
                value_table[item][weight] = value_table[item - 1][weight]

    return value_table[num_items][max_weight]

# Test the function
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
max_weight = 7
print(knapsack(weights, values, max_weight))  # Output: 9

# Explanation
# Initialization:
# value_table is a 2D list initialized with zeros. It has dimensions (number of items + 1) x (max weight + 1) to account for all items and capacities.
# Filling the Table:
# For each item and each possible weight capacity:
# If the item’s weight is less than or equal to the current capacity, you have two choices:
# Include the item: Add its value to the maximum value you can achieve with the remaining capacity.
# Exclude the item: Keep the maximum value without including this item.
# Update the table with the maximum value of these two choices.
# If the item’s weight is greater than the current capacity, you can’t include it, so just carry forward the value from the previous item.
# Result:
# The value at the bottom-right corner of the table (value_table[num_items][max_weight]) 
# represents the maximum value you can achieve with the given items and backpack capacity.
