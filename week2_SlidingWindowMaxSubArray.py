#Create a function that finds the maximum sum of a subarray with a given size
#Write a function called max_subarray_sum(arr, k) where arr is a list of integers and k is the size of the subarray.
#Use the sliding window technique to find the maximum sum of a subarray of size k.
#Return the maximum sum.arr = [2, 1, 5, 1, 3, 2]  and k = 3, the function should return 9 (5 + 1 + 3)

def max_subarray_sum(arr, k):
    max_sum = 0  #This will store the maximum sum we've found.
    current_sum = 0 #This will store the sum of the current window.
    
    # Initial window
    for i in range(k):
        current_sum += arr[i]
    
    max_sum = current_sum
    
    # Sliding window
    for i in range(k, len(arr)):
        current_sum = current_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example usage
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_subarray_sum(arr, k))  # Output should be 9

#another solution

def max_subarray_sum(arr, k):
    max_sum = 0

    for i in range(len(arr) - k + 1):
        current_sum = sum(arr[i:i + k])
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

# Example usage
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_subarray_sum(arr, k))  # Output should be 9


##############################################################################
#Another  solution

def max_subarray_sum(arr, k):

    max_sum = 0

    window_sum = 0

    window_start = 0

 

    for window_end in range(len(arr)):

        window_sum += arr[window_end]  # Add the next element

        if window_end >= k - 1:

            max_sum = max(max_sum, window_sum)

            window_sum -= arr[window_start]  # Subtract the element going out

            window_start += 1  # Slide the window ahead

 

    return max_sum

 

# Explanation:

# Function Definition:
# def max_subarray_sum(arr, k): defines a function named max_subarray_sum that takes two parameters:
# arr: A list of integers.
# k: The size of the subarray.
# Initialize Variables:
# max_sum = 0: This variable will store the maximum sum of any subarray of size k found so far.
# window_sum = 0: This variable will store the sum of the current sliding window.
# window_start = 0: This variable marks the start of the current sliding window.
# Iterate Through the Array:
# for window_end in range(len(arr)): starts a loop that iterates over each element in the array using the index window_end.
# Add the Next Element to the Window Sum:
# window_sum += arr[window_end]: Adds the current element (arr[window_end]) to the window_sum.
# Check if the Window Has Reached the Desired Size:
# if window_end >= k - 1: checks if the sliding window has reached the size k.
# This condition ensures that we only start calculating the sum and sliding the window once the window is large enough.
# Update the Maximum Sum:
# max_sum = max(max_sum, window_sum): Updates max_sum to be the maximum of the current max_sum and the window_sum.
# Slide the Window:
# window_sum -= arr[window_start]: Subtracts the element at the start of the window (arr[window_start]) from window_sum. 
# This is because the window is about to slide to the right, and this element will no longer be part of the window.
# window_start += 1: Moves the start of the window one step to the right.
# Return the Maximum Sum:
# return max_sum: After the loop completes, returns the maximum sum of any subarray of size k found.
# Example Walkthrough:

# Let’s walk through an example with arr = [2, 1, 5, 1, 3, 2] and k = 3:

# Initial State:
# max_sum = 0
# window_sum = 0
# window_start = 0
# First Iteration (window_end = 0):
# window_sum += arr[0] -> window_sum = 2
# window_end < k - 1 (0 < 2), so the condition is false.
# Second Iteration (window_end = 1):
# window_sum += arr[1] -> window_sum = 3
# window_end < k - 1 (1 < 2), so the condition is false.
# Third Iteration (window_end = 2):
# window_sum += arr[2] -> window_sum = 8
# window_end >= k - 1 (2 >= 2), so the condition is true.
# max_sum = max(0, 8) -> max_sum = 8
# window_sum -= arr[0] -> window_sum = 6
# window_start += 1 -> window_start = 1
# Fourth Iteration (window_end = 3):
# window_sum += arr[3] -> window_sum = 7
# window_end >= k - 1 (3 >= 2), so the condition is true.
# max_sum = max(8, 7) -> max_sum = 8
# window_sum -= arr[1] -> window_sum = 6
# window_start += 1 -> window_start = 2
# Fifth Iteration (window_end = 4):
# window_sum += arr[4] -> window_sum = 9
# window_end >= k - 1 (4 >= 2), so the condition is true.
# max_sum = max(8, 9) -> max_sum = 9
# window_sum -= arr[2] -> window_sum = 4
# window_start += 1 -> window_start = 3
# Sixth Iteration (window_end = 5):
# window_sum += arr[5] -> window_sum = 6
# window_end >= k - 1 (5 >= 2), so the condition is true.
# max_sum = max(9, 6) -> max_sum = 9
# window_sum -= arr[3] -> window_sum = 5
# window_start += 1 -> window_start = 4


############################################################################
#Another Solution
def max_subarray_sum(arr, k):

    max_sum = float('-inf') # to handle negative values
    window_sum = 0 #track of the sum of the current window

    for i in range(len(arr)):# A for loop iterates over each element in the array arr.
        window_sum += arr[i]  #For each element arr[i], it adds the value to window_sum
        if i >= k - 1: # checks if the index of I has reached the end of the first window of size k e.g if k = 3 this condition will be true when I is 2 (because we started the count from the index of 0)
            max_sum = max(max_sum, window_sum)# this line ensures max_sum always holds the highest value encountered
            window_sum -= arr[i - (k - 1)] # this line slides the window by subtracting the element that is left as the window moves forward. Eg if I = 2 and k = 3 it subtracts arr[0] from window_sum to prepare for next window

    return max_sum

 

# Test the function

arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_subarray_sum(arr, k))  # Output: 9

 

 

 

# Let’s walk through an example with arr = [2, 1, 5, 1, 3, 2] and k = 3:

# Initialization:
# Python

# max_sum = float('-inf')
# window_sum = 0
# AI-generated code. Review and use carefully. More info on FAQ.

# First Window:
# i = 0: window_sum = 2
# i = 1: window_sum = 2 + 1 = 3
# i = 2: window_sum = 3 + 5 = 8
# i >= k - 1 (2 >= 2) is true.
# max_sum = max(float('-inf'), 8) = 8
# window_sum -= arr[0] → window_sum = 8 - 2 = 6
# Second Window:
# i = 3: window_sum = 6 + 1 = 7
# i >= k - 1 (3 >= 2) is true.
# max_sum = max(8, 7) = 8
# window_sum -= arr[1] → window_sum = 7 - 1 = 6
# Third Window:
# i = 4: window_sum = 6 + 3 = 9
# i >= k - 1 (4 >= 2) is true.
# max_sum = max(8, 9) = 9
# window_sum -= arr[2] → window_sum = 9 - 5 = 4
# Fourth Window:
# i = 5: window_sum = 4 + 2 = 6
# i >= k - 1 (5 >= 2) is true.
# max_sum = max(9, 6) = 9
# window_sum -= arr[3] → window_sum = 6 - 1 = 5
# Final Result
# The function returns 9, which is the maximum sum of any subarray of size k in the array [2, 1, 5, 1, 3, 2].