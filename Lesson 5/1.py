import collections


while True:
    try:
        n = int(input('Введите количество компаний: '))
    except ValueError:
        print('Вы ввели недопустимое значение')
        continue
    break


companies = collections.defaultdict()
good_profit = collections.deque()
bad_profit = collections.deque()
all_profit = 0
quart = 4


for i in range(n):
    name = input(f'\nВведите название {i+1}-ой компании: ')
    profit = 0
    q = 1
    while q <= quart:
        try:
            profit += float(input(f'Введите прибыль за {q}й квартал: '))
        except ValueError:
            print('Вы ввели недопустимое значение')
            continue
        q += 1
    companies[name] = profit
    all_profit += profit


mid_profit = all_profit / n
for i, item in companies.items():
    if item >= mid_profit:
        good_profit.append(i)
    else:
        bad_profit.append(i)


print(f'\n Средняя прибыль для всех компаний составила: {mid_profit}')

print(f'Прибыль выше среднего у {len(good_profit)} компаний:')
for name in good_profit:
    print(name)

print(f'Прибыль ниже среднего у {len(bad_profit)} компаний:')
for name in bad_profit:
    print(name)
