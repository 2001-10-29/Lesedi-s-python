from double_vowel import double_vowel 
def funny_phrase(phase):
    words = phase.split()
    result = []
    for word in words:
        result.append(double_vowel(word))
    return " ".join(result)

print(funny_phrase("she dreamed of being a runner"))
# 'she dreeaameed of beeiing a ruunneer'

print(funny_phrase("park near the stoplight"))
# 'park neeaar the stoopliight'

print(funny_phrase("we need many gardeners"))
# 'we neeeed many gaardeeneers'

