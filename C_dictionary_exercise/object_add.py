def object_add(obj1, obj2):
    result = {}
    for key in set(obj1.keys()).union(set(obj2.keys())):
        result[key] = obj1.get(key, 0) + obj2.get(key, 0)
    return result

obj1 = {"x":3,"y":10 }
obj2 = {"y":2,"x":1 }

print(object_add(obj1, obj2))
# { "x": 4, "y": 12 }


obj3 = {"a":3,"b":2,"c": -1 }
obj4 = {"b":5,"c":1,"e":4 }

print(object_add(obj3, obj4))
# { "a": 3, "b": 7, "c": 0, "e": 4 }

