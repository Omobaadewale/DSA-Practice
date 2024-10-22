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


