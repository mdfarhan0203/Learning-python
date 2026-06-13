# 1. Reverse a String
# Write a function to reverse a string.

def reverseString(s):
    return s[::-1]

print(reverseString("Deloitte"))




# 2. Check for Palindrome
# Write a function to check if a string is a palindrome.
def is_palindrome(x):
    return x == x[::-1]



print(is_palindrome("radar"))   # True
print(is_palindrome("Deloitte"))  # Output: False




#3. Find the Maximum Element in a List
# Write a function to find the maximum element in a list.

def find_max(x):
    return max(x)

print(find_max([3, 5, 70, 2, 8]))  



# 4. Fibonacci Sequence
# Write a function to generate the first n Fibonacci numbers.

