# Write a function `remove_last_vowel` that accepts a string as an argument.
# The function should return the string with its last vowel removed.
# Vowels are the letters: a, e, i, o, u

def remove_last_vowel(word):
    vowels = "aeiou"

    # go through the word backwards
    for i in range(len(word) - 1, -1, -1):
        if word[i] in vowels:
            return word[:i] + word[i+1:]

    return word
        
print(remove_last_vowel("speaker"))# 'speakr'
print(remove_last_vowel("trading"))# 'tradng'
print(remove_last_vowel("thunder"))# 'thundr'
print(remove_last_vowel("myth"))# 'myth'

