from random import randint
import sys

'''
Я пытался сделать вывод размеров с помощью декоратора, но ничего дельного не вышло.
Также я не сичтал память, занимаемую функциями и locals, потому что в основных программах их, по факту, нет.

'''

'''
5-ое задание третьего урока
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
'''


def max_negative():
    num_list = [randint(-10, 10) for _ in range(10)]

    negative = [num for num in num_list if num < 0]

    for key, value in locals().items():
        print(f'object = {key} : {value}; type = {type(value)}, size = {sys.getsizeof(value)}')

    return (f'\n В массиве: \n{num_list} \nмаксимальный отрицательный элемент = {max(negative)} \n'
            f'его индекс = {num_list.index(max(negative))}')


print(max_negative(), "\n" * 2)  # Добавил отступ, чтобы не слипалось со следующим заданием

'''
object = num_list : [-8, -10, -5, -1, -7, 7, 2, -5, -8, 7]; type = <class 'list'>, size = 92
object = negative : [-8, -10, -5, -1, -7, -5, -8]; type = <class 'list'>, size = 60
'''

'''
Наверное надо учитывать и num в генераторе, но я не знаю, как нормально вывести его размер.
Но судя по тому, что там максимум 10/-10, которые при отдельной проверки дают размер 14,
я не думаю, что там может получиться что-то больше.
'''


'''
9-ое задание третьего урока
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''


def max_elem():
    matrix = [[randint(1, 10) for _ in range(4)] for _ in range(4)]

    mines = []
    for idx in range(4):
        min_el = matrix[0][idx]
        for line in matrix:
            if line[idx] < min_el:
                min_el = line[idx]
        mines.append(min_el)

    print("В матрице")
    for matrix_line in matrix:
        print('|  {}  {}  {}  {}  |'.format(*line))
    print(f'Максимальный элемент среди минимальных элементов столбцов = {max(mines)} \n')

    for key, value in locals().items():
        print(f'object = {key} : {value}; type = {type(value)}, size = {sys.getsizeof(value)}')
    return "\n"  # Сделал так просто чтобы не принтовало None


print(max_elem())
'''
object = matrix : [[10, 10, 3, 6], [3, 6, 10, 6], [5, 6, 8, 1], [1, 3, 9, 9]]; type = <class 'list'>, size = 44
object = mines : [1, 3, 3, 1]; type = <class 'list'>, size = 44
object = idx : 3; type = <class 'int'>, size = 14
object = min_el : 1; type = <class 'int'>, size = 14
object = line : [1, 3, 9, 9]; type = <class 'list'>, size = 44
object = matrix_line : [1, 3, 9, 9]; type = <class 'list'>, size = 44
'''

'''
Смотря по id элементов циклов, они при каждой итерации занимают разные слоты памяти.
Наверое, размеры idx, min_el, line и matrix_line должны быть в n (длина строки матрицы) раз больше,
но предположу, что сохраняется лишь последняя итерация, а остальное идёт в мусор.
В принципе, тоже самое и с генератором и num из другого задания.
'''

'''
Мне кажется, что matrix весит, всё же больше, учитывая.
Судя по тому, что список из четырёх элементов весит 44, а здесь таких 4, он должен минимум в четыре раз быть больше?
Может надо всё изощерять до чего-то подобного...
'''


def max_elem_2():
    matrix = [[randint(1, 10) for _ in range(4)] for _ in range(4)]

    mines = []
    for idx in range(4):
        min_el = matrix[0][idx]
        for line in matrix:
            if line[idx] < min_el:
                min_el = line[idx]
        mines.append(min_el)

    print("В матрице")
    for matrix_line in matrix:
        print('|  {}  {}  {}  {}  |'.format(*line))
    print(f'Максимальный элемент среди минимальных элементов столбцов = {max(mines)} \n')

    for value in locals().values():
        print(f'object = {value}; type = {type(value)}, size = {sys.getsizeof(value)}')
        if isinstance(value, list):
            for arg in value:
                print(f'object = {arg}; type = {type(arg)}, size = {sys.getsizeof(arg)}')
                if isinstance(arg, list):
                    for i in arg:
                        print(f'object = {i}; type = {type(i)}, size = {sys.getsizeof(i)}')
        print("---")
    return "\n"  # Сделал так просто чтобы не принтовало None


print(max_elem_2())

'''
object = [[4, 6, 10, 9], [1, 6, 3, 9], [8, 3, 5, 10], [3, 6, 2, 3]]; type = <class 'list'>, size = 44
object = [4, 6, 10, 9]; type = <class 'list'>, size = 44
object = 4; type = <class 'int'>, size = 14
object = 6; type = <class 'int'>, size = 14
object = 10; type = <class 'int'>, size = 14
object = 9; type = <class 'int'>, size = 14
object = [1, 6, 3, 9]; type = <class 'list'>, size = 44
object = 1; type = <class 'int'>, size = 14
object = 6; type = <class 'int'>, size = 14
object = 3; type = <class 'int'>, size = 14
object = 9; type = <class 'int'>, size = 14
object = [8, 3, 5, 10]; type = <class 'list'>, size = 44
object = 8; type = <class 'int'>, size = 14
object = 3; type = <class 'int'>, size = 14
object = 5; type = <class 'int'>, size = 14
object = 10; type = <class 'int'>, size = 14
object = [3, 6, 2, 3]; type = <class 'list'>, size = 44
object = 3; type = <class 'int'>, size = 14
object = 6; type = <class 'int'>, size = 14
object = 2; type = <class 'int'>, size = 14
object = 3; type = <class 'int'>, size = 14
---
object = [1, 3, 2, 3]; type = <class 'list'>, size = 44
object = 1; type = <class 'int'>, size = 14
object = 3; type = <class 'int'>, size = 14
object = 2; type = <class 'int'>, size = 14
object = 3; type = <class 'int'>, size = 14
---
object = 3; type = <class 'int'>, size = 14
---
object = 3; type = <class 'int'>, size = 14
---
object = [3, 6, 2, 3]; type = <class 'list'>, size = 44
object = 3; type = <class 'int'>, size = 14
object = 6; type = <class 'int'>, size = 14
object = 2; type = <class 'int'>, size = 14
object = 3; type = <class 'int'>, size = 14
---
object = [3, 6, 2, 3]; type = <class 'list'>, size = 44
object = 3; type = <class 'int'>, size = 14
object = 6; type = <class 'int'>, size = 14
object = 2; type = <class 'int'>, size = 14
object = 3; type = <class 'int'>, size = 14
---
'''