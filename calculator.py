import math

def calculator():
    print("Advanced Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    ''' Optional Operations '''
    print("5. Power") 
    print("6. Square Root")
    print("7. Logarithm")

    choice = input("Enter choice (1-7): ")

    if choice not in ('1', '2', '3', '4', '5', '6', '7'):
        print("Invalid input. Please enter a valid number (1/2/3/4/5/6/7).")
        return

    num1 = float(input("Enter first number: "))
    num2 = None

    if choice in ('1', '2', '3', '4', '5', '7'):
        num2 = float(input("Enter second number: "))

    if choice == '4' and num2 == 0:
        print("Error: Division by zero")
        return

    if choice == '1':
        print(num1, "+", num2, "=", num1 + num2)
    elif choice == '2':
        print(num1, "-", num2, "=", num1 - num2)
    elif choice == '3':
        print(num1, "*", num2, "=", num1 * num2)
    elif choice == '4':
        print(num1, "/", num2, "=", num1 / num2)
    elif choice == '5':
        print(num1, "raised to the power of", num2, "=", num1 ** num2)
    elif choice == '6':
        if num1 >= 0:
            print("Square root of", num1, "=", math.sqrt(num1))
        else:
            print("Error: Square root of negative number")
    elif choice == '7':
        base = float(input("Enter logarithm base: "))
        if num1 > 0 and base > 0 and base != 1:
            print("Logarithm of", num1, "with base", base, "=", math.log(num1, base))
        else:
            print("Error: Invalid input for logarithm")

calculator()
