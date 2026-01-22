# Returns **True** if `str2` is found inside `str1`
# Ignore capitalization differences

def contains (str1, str2):
    str1_lower = str1.lower()
    str2_lower = str2.lower()
    return str2_lower in str1_lower

print(contains("caterpillar", "pill"))     # True
print(contains("lion's share", "on"))      # True
print(contains("SORRY", "or"))             # True
print(contains("tangent", "gem"))          # False
print(contains("clock", "ok"))             # False

