number1 = float(input('Enter first number: '))
number2 = float(input('Enter second number: '))
operator = input('Enter operator (+, -, *, /): ')
if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2
else:
    result = None
print(f'{number1} {operator} {number2} = {result}')
