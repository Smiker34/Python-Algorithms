from random import randint

array = [randint(0, 100) for _ in range(10)]
even = [i for i, item in enumerate(array) if item % 2 == 0]

print(f'Для массива: \n{array}\nИндексы четных элементов: \n{even}')