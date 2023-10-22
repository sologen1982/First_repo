def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def number_of_groups(n, k):
    if n < k:
        raise ValueError("The total number of people should be greater than or equal to the number of winners.")
    
    combinations = factorial(n) / (factorial(n - k) * factorial(k))
    return int(combinations)

# Приклад використання
total_people = 2
winners = 1

result = number_of_groups(total_people, winners)
print(f"There are {result} different groups of winners.")
    