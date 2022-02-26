print('Ведите 3 разных числа:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

print(f'Число {(a + b + c) - max(a, b, c) - min(a, b, c)} - среднее')