print('Введите длину последовательности и цифру, которую хотите подсчитать: ')

length = int(input('Длина = '))
num = input('Цифра = ')
count = 0

for i in range(length):
    number = input(f'Введите {i+1}-е число: ')
    for k in number:
        if k == num:
            count += 1

print(f'Число {num} встречается в последовательности {count} раз')