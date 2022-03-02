matrix = [[] for _ in range(4)]

for line in matrix:
    num = input('Введите 4 числа через запятую: ')
    line.extend(int(i) for i in num.split(','))
    line.append(sum(line))

for line in matrix:
    print('|  {}  {}  {}  {}  {}  |'.format(*line))