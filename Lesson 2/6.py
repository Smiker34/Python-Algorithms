from random import randint

number = randint(0, 101)
for i in range(10):
    num = int(input('Угадайте целое число от 0 до 100: '))
    if num == number:
        print('Поздравляем, вы угадали!')
        break
    elif num < number:
        print('Ваше число меньше загаданного')
    else:
        print('Ваше число больше загаданного')
print(f'Было загадано число {number}')