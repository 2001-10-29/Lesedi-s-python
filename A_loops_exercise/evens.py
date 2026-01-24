# Write a function `evens(max_num)` that prints all positive even numbers LESS than max_num.

def evens(max_num):
    for num in range(2, max_num, 2):
        print(num)

evens(11)
evens(8)

