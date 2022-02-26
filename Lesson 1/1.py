
num = int(input("Введите трёхзначное число: "))

a = num // 100
b = (num % 100) // 10
c = num % 10

summ = a + b + c
mul = a * b * c

print("Сумма - {0}, Произведение {1}.".format(summ, mul))
