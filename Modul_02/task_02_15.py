def calculate(operand, operator, result):
    if operator == '+':
        result += operand
    elif operator == '-':
        result -= operand
    elif operator == '*':
        result *= operand
    elif operator == '/':
        if operand == 0:
            raise ValueError("Cannot divide by zero")
        result /= operand
    return result


def main():
    result = None
    operand = None
    operator = None
    wait_for_number = True


    try:
        while True:
            if wait_for_number:
                user_input = input("Enter a number: ")
                operand = float(user_input)
                wait_for_number = False
            else:
                user_input = input("Enter an operator (+, -, *, /) or '=' to calculate: ")
                if user_input in ('+', '-', '*', '/'):
                    if operator is not None:
                        print(f"{operator} is not a number. Try again.")
                        continue
                    operator = user_input
                    wait_for_number = True
                elif user_input == '=':
                    if operator is None:
                        print("No operator entered. Try again.")
                        continue
                    result = calculate(operand, operator, result)
                    print(f"Result: {result}")
                    break
                else:
                    print(f"{user_input} is not an operator. Try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
