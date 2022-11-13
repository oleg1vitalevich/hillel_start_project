x = int(input('Enter the first number \n'))
y = int(input('Enter the second number \n'))
c = input('Enter operation \n')

if c == '+':
    result = x + y
    print(result)
elif c == '-':
    result = x - y
    print(result)
elif c == 'pow':
    result = pow(x, y)
    print(result)
elif c == '*':
    result = x * y
    print(result)
elif c == '/':
    result = x / y
    print(result)
else:
    print("Im sorry, I can't count")
