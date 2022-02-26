a = float(input('Введите первое число или 0 для выхода:'))
while a != 0.:
    b = float(input('Введите второе число: '))
    oper = input('Введите действие (+, -, *, /): ')

    if oper == '+':
        print(f'{a}{oper}{b} = {a + b}')
    elif oper == '-':
        print(f'{a}{oper}{b} = {a - b}')
    elif oper == '*':
        print(f'{a}{oper}{b} = {a * b}')
    elif oper == '/':
        if b != 0:
            print(f'{a}{oper}{b} = {a / b}')
        else:
            print('На ноль делить нельзя')
    else:
        print('Неверный ввод действия')

    a = float(input('Введите первое число или 0 для выхода:'))