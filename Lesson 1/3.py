print('Ведите координаты 2х точек:')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

a = y2 - y1
b = x1 - x2
c = x2 * y1 - x1 * y2
if a == 0 and b == 0:
    print('Точки совпадают')
elif a == 0:
    print(f'Уравнение прямой:\n'
          f'{b}y + {c} = 0')
elif b == 0:
    print(f'Уравнение прямой:\n'
          f'{a}x + {c} = 0')
else:
    print(f'Уравнение прямой:\n'
          f'{a}x + {b}y + {c} = 0')