from random import randint

num_list = [randint(0, 100) for _ in range(10)]
print(num_list)

max_idx = num_list.index(max(num_list, key=lambda i: int(i)))
min_idx = num_list.index(min(num_list, key=lambda i: int(i)))

num_list[max_idx], num_list[min_idx] = num_list[min_idx], num_list[max_idx]

print('Переставим максимальный и минимальный элементы:\n', num_list)