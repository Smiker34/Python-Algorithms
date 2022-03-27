from random import shuffle


def merge_sort(lst):

    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        merge_sort(left)
        merge_sort(right)
        left_idx = right_idx = lst_idx = 0  # Наверное стоило просто обозначить буквами и сделать пояснение комментарием

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                lst[lst_idx] = left[left_idx]
                left_idx += 1
            else:
                lst[lst_idx] = right[right_idx]
                right_idx += 1
            lst_idx += 1

        while left_idx < len(left):  # Если левая часть больше
            lst[lst_idx] = left[left_idx]
            left_idx += 1
            lst_idx += 1

        while right_idx < len(right):   # Если правая часть больше
            lst[lst_idx] = right[right_idx]
            right_idx += 1
            lst_idx += 1


lst = [_ for _ in range(50)]
shuffle(lst)
print(f'Список до сортировки: \n{lst}')
merge_sort(lst)
print(f'Список после сортировки: \n{lst}')
