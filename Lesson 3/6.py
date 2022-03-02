from random import randint

num_list = [randint(0, 10) for _ in range(10)]
print(num_list)

"""
 max - вызов генератора, который через обратный порядок индексов,
 выдаёт последнее вхождение значения (просто, что я понимаю, что пишу)
 Надеюсь достаточно читаемо.
"""

max_idx = next(i for i in reversed(range(len(num_list)))
               if num_list[i] == max(num_list, key=lambda i: int(i)))
min_idx = num_list.index(min(num_list, key=lambda i: int(i)))

print(f'Минимальный элемент = {num_list[min_idx]} (индекс {min_idx})\n'
      f'Максимальный элементам = {num_list[max_idx]} (индекс {max_idx})')

print(f'Элементы между минимальным и максимальным: {num_list[min_idx + 1:max_idx]}')

summa = 0
for i in range(min_idx + 1, max_idx):
    summa += num_list[i]

print(f'Сумма элементов, находящихся между минимальным и максимальным элементами = {summa}')