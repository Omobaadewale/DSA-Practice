# Challenge: Container With Most Water
# Problem Statement: You are given an array height of positive integers where each integer represents the height of a vertical line on a coordinate plane. 
# The lines are drawn such that the two endpoints of the line at index i are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.
# Explanation: The vertical lines are drawn at indices 0, 1, 2, 3, 4, 5, 6, 7, and 8. The two lines that form the container with the most water are at indices 1 and 8,
# with a height of 8 and 7 respectively. 
# The container can store 49 units of water


def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        # Calculate the area
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        max_area = max(max_area, current_area)

        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Example usage
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = maxArea(height)
print(result)

# Example Walkthrough
# Let’s walk through an example with the array [1, 8, 6, 2, 5, 4, 8, 3, 7]:

# Initial State:
# left = 0 (height = 1)
# right = 8 (height = 7)
# Width: 8 - 0 = 8
# Height: min(1, 7) = 1
# Area: 8 * 1 = 8
# Max Area: 8
# Move Left Pointer (since height[left] < height[right]):
# left = 1 (height = 8)
# Width: 8 - 1 = 7
# Height: min(8, 7) = 7
# Area: 7 * 7 = 49
# Max Area: 49
# Move Right Pointer (since height[left] >= height[right]):
# right = 7 (height = 3)
# Width: 7 - 1 = 6
# Height: min(8, 3) = 3
# Area: 6 * 3 = 18
# Max Area: 49
# Continue Moving Pointers:
# Repeat the process, updating the pointers and calculating the area each time.
# The maximum area found remains 49.
# Conclusion
# By using the two-pointer technique, we efficiently find the maximum area in O(n) time complexity. This approach ensures we consider all possible containers without needing to check every pair of lines, which would be less efficient.



