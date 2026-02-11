# take 2 number int(input())
# take Operation
# print result
#import numbers
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
op = input("Enter the operator (+, -, *, /): ")

if op == "+":
    print("Result:", num1 + num2)

elif op == "-":
    print("Result:", num1 - num2)

elif op == "*":
    print("Result:", num1 * num2)

elif op == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed")
    else:
        print("Result:", num1 / num2)
else:
    print("Invalid operator")
