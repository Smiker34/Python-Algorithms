from random import shuffle


def bubble_sort(lst, reverse=False):

    if reverse:
        left = 1
        right = 0
    else:
        left = 0
        right = 1

    length = len(lst)
    n = 1

    while n < length:
        count = True
        for idx in range(n-1, length-n):
            if lst[idx+left] > lst[idx + right]:
                lst[idx], lst[idx+1] = lst[idx+1], lst[idx]
                count = False
        if count:
            break
        for idx in range(length-n, n-1, -1):
            if lst[idx-left] < lst[idx - right]:
                lst[idx], lst[idx-1] = lst[idx-1], lst[idx]
        n += 1


lst = [_ for _ in range(-100, 100)]
shuffle(lst)
print(f'Список до сортировки: \n{lst}')
bubble_sort(lst)
print(f'Список после сортировки: \n{lst}')
