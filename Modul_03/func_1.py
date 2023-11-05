def my_sum(a, b):
    return a + b

print(my_sum(1, 2))


def my_sum_2(a, b):
    print(f"A: {a}, B: {b}")

args = [1, 2]

my_sum_2(*args)     # * распаковывает: списки, кортежи, строки


def my_sum_3(a, b):
    print(f"A: {a}, B: {b}")

args = { "a": 3, "b": 4}

my_sum_3(**args)     # ** распаковывает: словари dict



def my_sum(*numbers):
    print(numbers)
    res = 0
    for i in numbers:
        res += i
    return res
    
print(my_sum(1, 2, 3, 4))


def print_sums(**args):
    print(args)

    for key, value in args.items():
        print(f"{key}: {my_sum(*value)}")

print_sums(
    first=[1, 2, 3],
    second=[5, 6, 7]
)
    
def print_name(name):
    print(name)

client_name = input("Say your name: ")
print_name(client_name)    