a = int(input("Enter a: "))
b = int(input("Enter b: "))
oper = input("Enter operator: ")

if oper == "+":
    c = a + b
elif oper == "-":
    c = a - b
elif oper == "*":
    c = a * b
elif oper == "/":
    c = a / b
else:
    print("Incorrect operator")
    exit(1)

print(f"Result is: {c}")




