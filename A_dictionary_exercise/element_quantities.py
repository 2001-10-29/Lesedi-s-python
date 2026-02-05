def element_quantities(dict1):
    result = []
    for key, value in dict1.items():
        result.extend([key] * value)
    return result

quantities1 = {"cat":3,"bird":1,"dog":2 }
print(element_quantities(quantities1))
# ['cat', 'cat', 'cat', 'bird', 'dog', 'dog']

quantities2 = {"blue":3,"brown":1 }
print(element_quantities(quantities2))
# ['blue', 'blue', 'blue', 'brown']

