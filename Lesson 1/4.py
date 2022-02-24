from random import randint, uniform

print('Ведите границы для случайного целого числа:')
x1 = int(input('x1 = '))
x2 = int(input('x2 = '))

print('Ведите границы для случайного вещественного числа:')
y1 = float(input('y1 = '))
y2 = float(input('y2 = '))

print('Ведите границы для случайной буквы:')
ch1 = input('char1 = ').upper()
ch2 = input('char2 = ').upper()

print(f'Случайное целое число: {randint(x1, x2)}\n'
      f'Случайное вещественное число: {round(uniform(y1, y2),3)}\n'
      f'Случайная буква: "{chr(randint(ord(ch1), ord(ch2)))}"')