# Write a function `no_ohs(text)` that prints each character of the string except 'o'.
# The function does not return a value, just prints.

def no_ohs(text):
    for char in text:
        if char != 'o':
            print(char)

no_ohs("code") 
# c
# d
# e

