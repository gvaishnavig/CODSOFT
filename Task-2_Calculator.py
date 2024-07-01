def getNumber(number):
    while True:
        try:
            return float(input(number))
        except ValueError:
            print("Invalid input. Please enter a number.")

def getOperation():
    while True:
        operation = input("Choose an operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Invalid operation. Please choose one of +, -, *, /")

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            print("Error! Division by zero.")

def main():
    print("CALCULATOR")
    num1 = getNumber("Enter the first number: ")
    num2 = getNumber("Enter the second number: ")
    operation = getOperation()
    result = calculate(num1, num2, operation)
    print(f"The result of {num1} {operation} {num2} = {result} \n")

if __name__ == "__main__":
    main()