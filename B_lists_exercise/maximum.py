# Write a function `maximum(numbers)` that accepts a list of numbers.
# The function should return the largest number in the list.
# If the list is empty, return None.

def maximum(numbers):
    if not numbers:
        print('none')
    else:
        max_num = numbers[0]
        for number in numbers:
            if number > max_num:
                max_num = number
                print(max_num)


maximum([5, 6, 3, 7]) #-> 7
maximum([17, 15, 19, 11, 2]) #-> 19
maximum([]) #-> None

