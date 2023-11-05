def recursive_sum(*items):
    if len(items) == 1:
        return items[0]
    return items[0] + recursive_sum(*items[1:])
    
print(recursive_sum(1, 2, 3))
    