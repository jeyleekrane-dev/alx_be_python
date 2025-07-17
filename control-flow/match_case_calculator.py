num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Choose the operation (+,-,*,/): ")

# strinh conversion to integer

num1 = int(num1)
num2 = int(num2)

# match case operations

match operation:
    case '+':
        print(f"The result is {num1+num2}")
    case '-':
        print(f"The result is {num1-num2}")
    case '*':
        print(f"The result is {num1*num2}.")
    case '/':
        if num2 == 0 and operation == '/':
            print("Cannot divide by zero.")
        else:
            print(f"The resul1t is {num1/num2}.")
    case'_':
        print("please enter a valid operator")
