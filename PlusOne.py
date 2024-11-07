
#my own code
def plusone(arr):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i - 1] += 1
    
    # Handle the case where the first digit becomes 10
    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)
    
    return arr

# Example usage
arr = [1, 2, 3]
output = plusone(arr)
print(output)  # Output: [1, 2, 4]

#I like this code

def plus_one(digits):
    # Step 1: Combine the digits into a number
    num = 0
    for digit in digits:
        num = num * 10 + digit
    
    # Step 2: Add one to the number
    num += 1
    
    # Step 3: Split the new number back into digits
    result = [int(digit) for digit in str(num)]
    
    return result

# Example usage
digits = [1, 2, 3]
output = plus_one(digits)
print(output)  # Output: [1, 2, 4]

#seems optimal
def plus_one(digits):
    #int(...): This converts the string '123' to the integer 123.
    # Convert the list of digits to a single integer # ''.join(...): This joins the list of strings into a single string. For example, ['1', '2', '3'] becomes '123'.
    num = int(''.join(map(str, digits))) #map(str, digits): This converts each integer in the list digits to a string. For example, [1, 2, 3] becomes ['1', '2', '3'].
    
    # Increment the integer by one
    num += 1

# result = [int(digit) for digit in str(num)]
# str(num): This converts the integer 124 back to a string '124'.
# [int(digit) for digit in str(num)]: This is a list comprehension that converts each character in the string '124' back to an integer. So, '1', '2', and '4' become [1, 2, 4].
    # Convert the integer back to a list of digits
    result = [int(digit) for digit in str(num)]
    
    return result

# Example usage
digits = [1, 2, 3]
output = plus_one(digits)
print(output)  # Output: [1, 2, 4]





