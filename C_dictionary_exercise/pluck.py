def pluck(dictionary, key):
    plucked = {}
    for k in key:
        if k in dictionary:
            plucked[k] = dictionary[k]
    return plucked

print(pluck(
    {"name":"Fido","color":"Brown","breed":"German Shepherd" },
    ["name","breed"]
))
# { "name": "Fido", "breed": "German Shepherd" }

print(pluck(
    {"make":"Tesla","mpg":93,"model":"Model X","color":"white" },
    ["make","model"]
))
# { "make": "Tesla", "model": "Model X" }

