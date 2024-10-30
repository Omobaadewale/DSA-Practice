

def length_of_longest_substring(s):

    max_length = 0 #keeps track of the max lenght of the substrings found
    current_window = {} # tracks the last seen index of each character
    start = 0 # track sthe starting index of the current window

 

    for end in range(len(s)): # for eeach character in s at index i
        if s[end] in current_window and current_window[s[end]] >= start:# if char in currentwindow and its index is within current window, move start to the right of the previous index of the char
            start = current_window[s[end]] + 1 #update the last seen index of the current char  

        current_window[s[end]] = end
        max_length = max(max_length, end - start + 1) # calculate the len of the current window and update maxlen

 

    return max_length

 

# Example usage

s = "abcabcbb"

print(length_of_longest_substring(s))  # Output: 3

# Brute force

def length_of_longest_substring(s):

    max_length = 0
    current_window = {}
    start = 0

    for end in range(len(s)):

        if s[end] in current_window and current_window[s[end]] >= start:
            start = current_window[s[end]] + 1
        current_window[s[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length

# Example usage
s = "abcabcbb"
print(length_of_longest_substring(s))  # Output: 3