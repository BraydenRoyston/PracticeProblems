print("Welcome to 'Does it Divide?'")
print("This program can check if a number is even, or it can check if a number is divisible by another number.")
print("Enter what you want the program to do (enter 'even' or 'factor check')")
response = input()

if response == "even":
    print("Welcome to the even check!")
    num1 = float(input("Enter the number you wish to check:"))

    if num1 % 2 == 0:
        print(str(num1) + " is an even number!")
    else:
        print(str(num1) + " is not an even number.")


if response == "factor check":
    print("Welcome to the factor check!")
    num1 = float(input("Enter the number you wish to divide:"))
    num2 = float(input("Enter the number you wish to divide the first number by:"))

    if num1 % num2 == 0:
        print(str(num1) + " is divisible by " + str(num2) + "!")
    else:
        print(str(num1) + " is not divisible by " + str(num2) + ".")