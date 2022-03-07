'''
5-ое задание третьего урока
В обоих случаях, если я всё правильно понял, будет О(n),
где n - длина генерируемого списка.
'''

from random import randint
import timeit

# Первый вариант (быстрее с ростом n)
start_time = timeit.default_timer()

num_list = [randint(-10, 10) for _ in range(10)]

negative = [num for num in num_list if num < 0]

print(f'В массиве: \n{num_list} \nмаксимальный отрицательный элемент = {max(negative)} \n'
      f'его индекс = {num_list.index(max(negative))}')

print(timeit.default_timer() - start_time, "\n")


# Второй вариант (Медленнее с ростом n)
start_time = timeit.default_timer()

num_list = [randint(-10, 10) for _ in range(10)]
min_el = -float('inf')

for i, item in enumerate(num_list):
    if min_el < item < 0:
        min_el = item
        min_idx = i

print(f'В массиве: \n{num_list} \nминимальный отрицательный элемент = {min_el} \n'
      f'его индекс = {min_idx}')

print(timeit.default_timer() - start_time)
