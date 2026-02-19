# Write a function `lala_language` that accepts a sentence string as an argument.
# The function should return a new sentence where words longer than 3 characters
# are modified.
#
# Modified words should have each vowel followed by 'l' and the same vowel again.
# See the examples below.

def lala_language(sentence):
    vowels = "aeiou"
    words = sentence.split()
    new_words = []

    for word in words:
        # only change words longer than 3 letters
        if len(word) > 3:
            new_word = ""
            for letter in word:
                if letter in vowels:
                    new_word += letter + "l" + letter
                else:
                    new_word += letter
            new_words.append(new_word)
        else:
            new_words.append(word)

    return " ".join(new_words)

print(lala_language('this is pretty strange'))
# 'thilis is preletty stralangele'

print(lala_language('can you speak our language'))
# 'can you spelealak our lalangulualagele'

