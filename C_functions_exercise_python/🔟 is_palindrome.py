# Write a function that checks if a string is a **palindrome** (same forward & backward).
# Ignore spaces and capitalization.

def is_palindrome(s):
    s_cleaned = s.replace(" ",' ' ).lower()
    return s_cleaned == s_cleaned[::-1] 



print(is_palindrome("level"))          # True
print(is_palindrome("Race car"))       # True
print(is_palindrome("python"))         # False

