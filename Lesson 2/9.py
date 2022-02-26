max_sum = 0
num = int(input('Введите целое число. Чтобы выйти введите 0.\nnum = '))

while num != 0:
    summa = 0
    n = num

    while num % 10 != 0 or num // 10 != 0:
        summa += num % 10
        num //= 10

    if summa > max_sum:
        max_sum = summa
        max_num = n

    num = int(input('Введите целое число. Чтобы выйти введите 0.\nnum = '))

print(f'У числа {max_num} наибольшая сумма цифр = {max_sum}')