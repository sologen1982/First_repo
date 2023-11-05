def calculate_1(*args):
    
    for arg in args:
        print(arg)
    return args

print(calculate_1(2, 3, 7))


def calculate_2(**kwargs):
    
    return kwargs

print(calculate_2(a=2, b=3, c=7))


def calculate_3(x, y, *args, c=2, d=4, **kwargs):
    
    print(args)
    print(kwargs)

print(calculate_3(3, 4, 5, 5, c=5, d=4, rfr=44))

    

    