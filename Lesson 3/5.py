from random import randint

num_list = [randint(-10, 10) for _ in range(10)]

negative = [num for num in num_list if num < 0]

print(f'В массиве: \n{num_list} \nмаксимальный отрицательный элемент = {max(negative)} \n'
      f'его индекс = {num_list.index(max(negative))}')