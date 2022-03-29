# my_first_calculator.py by AceLewis, refactored by drewuwu
while True:
    print('Welcome to this calculator!')
    print('It can add, subtract, multiply and divide whole numbers')

    num1 = int(input('Please choose your first number: '))
    sign = input('What do you want to do? +, -, /, or *: ')
    num2 = int(input('Please choose your second number: '))
    calculation = "{} {} {}".format(num1, sign, num2)

    if sign == "+":
        result = str(num1 + num2)
        print(calculation+ " = " +result)
    elif sign == "-":
        result = str(num1 - num2)
        print(calculation+ " = " +result)
    elif sign == "*":
        result = str(num1 * num2)
        print(calculation+ " = " +result)
    elif sign == "/":
        result = str(num1 / num2)
        print(calculation+ " = " +result)

    print("Thanks for using this calculator, goodbye :)")
