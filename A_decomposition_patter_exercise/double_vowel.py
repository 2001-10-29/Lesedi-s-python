def double_vowel(word):
    vowels = "aeiou"
    result = ""
    for char in word:
        result += char
        if char in vowels:
            result += char
    return result 

print(double_vowel("runner"))
# 'ruunneer'

print(double_vowel("stoplight"))
# 'stoopliight'

print(double_vowel("gardener"))
# 'gaardeeneer'

