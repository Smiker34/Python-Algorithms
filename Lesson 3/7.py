from random import randint

num_list = [randint(0, 10) for _ in range(10)]

min_el = min(num_list, key=lambda i: int(i))


if num_list.count(min_el) > 1:
    print(f'В массиве: \n{num_list} \nминимальные элементы равны и это: {min_el}')
else:
    print(f'В массиве: \n{num_list} \nминимальные элементы: {min_el} и {sorted(set(num_list))[1]}')