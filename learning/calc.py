#!/usr/bin/python3


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calc(num1, num2):
    for symbol in operations:
        print (symbol)

    operation = input("Operation?: ")
  
    if operation in operations:
        calc_function = operations[operation]
        return (operation, calc_function(num1, num2))

keepGoing = True
num1 =  float(input("What's the first number?: "))
num2 =  float(input("What's the second number?: "))

for symbol in operations:
    print (symbol)
    
operation = input("Operation?: ")

if operation in operations:
    ans = operations[operation](num1, num2)
    print(f"{num1} {operation} {num2} = {ans}")

    while keepGoing:
        choice = input("Do you want to run more operations? (y/n): ")

        if choice == "y":
            num3 =  int(input("What's the next number?: "))
            num1 = ans
            (operation, ans) = calc(num1, num3)
            print(f"{num1} {operation} {num3} = {ans}")
        else:
            keepGoing = False
    
    