print('Введите длины трех отрезков:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b >= c and a + c >= b and b + c >= a:
    if a == b or b == c or c == a:
        if a == b and a == c:
            print('Треугольник равносторонний')
        else:
            print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Это не треугольник')