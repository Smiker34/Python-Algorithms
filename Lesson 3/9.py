from random import randint

matrix = [[randint(1, 10) for _ in range(4)] for _ in range(4)]

mines = []
for idx in range(4):
    min_el = matrix[0][idx]
    for line in matrix:
        if line[idx] < min_el:
            min_el = line[idx]
    mines.append(min_el)

print("В матрице")
for line in matrix:
    print('|  {}  {}  {}  {}  |'.format(*line))
print(f'Максимальный элемент среди минимальных элементов столбцов = {max(mines)}')
