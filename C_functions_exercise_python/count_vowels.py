# Return how many vowels are in the string.

def count_vowels(s):
    vowels = 'aeiou'
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

print(count_vowels("hello"))        # 2
print(count_vowels("Programming"))  # 3

