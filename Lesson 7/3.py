from random import choice, randint


def median(lst, k):
    if len(lst) == 1:
        return lst[0]

    pivot = choice(lst)

    left_nums = [num for num in lst if num < pivot]
    right_nums = [num for num in lst if num > pivot]
    pivots = [num for num in lst if num == pivot]

    if k < len(left_nums):
        return median(left_nums, k)
    elif k < len(left_nums) + len(pivots):
        return pivots[0]
    else:
        return median(right_nums, k - len(left_nums) - len(pivots))


m = 5
lst = [randint(0, 20) for _ in range(2 * m + 1)]

print(f'Исходный список:\n{lst}')
print(f'Медианой списка является:\n{median(lst, len(lst) // 2)}')

lst.sort()
print(f'Проверка!\nСписок после сортировки:\n{lst}')
print(f'Медианой списка является:\n{lst[len(lst) // 2]}')