# facem un calculator
# booon ... definim functiile


def add(x, y):
    return int(x + y)


def substract(x, y):
    return int(x - y)


def multiply(x, y):
    return int(x * y)


def divide(x, y):
    return int(x // y)


# input de la user
num1 = input("Enter first Number(or a letter to exit): ")
try:
    num1 = int(num1)
except ValueError:
    exit()

choice = input("Enter an operation: ")
num2 = int(input("Enter 2nd Number: "))


if choice == '+':
    print('Result:', add(num1, num2))

if choice == '-':
    print('Result:', substract(num1, num2))
if choice == '*':
    print('Result:', multiply(num1, num2))

if choice == '/':
    print('Result:', divide(num1, num2))
