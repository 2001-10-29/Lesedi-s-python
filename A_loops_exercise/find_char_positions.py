# Write a function that prints all indexes where a character appears in a string.

def find_char_positions(string, char):
    for index in range (len(string)):
        if string [index] == char:
            print(index)
            
find_char_positions("banana", "a")
# 1
# 3
# 5

