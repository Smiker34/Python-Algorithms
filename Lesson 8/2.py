from collections import Counter
"""
Явно не лучшее решение, но реализовать это как-то правильней и элегатней
через класс, который представлял бы из себя узлы,
и какую-нибудь рекурсивную функцию, которая на одну ветвь давала значение, а на другую вызывала себя,
у меня до конца не вышло. Дерево, теоретически, выстраивается, но как достать из него кодировки - ноль идей.
P.S. Кажется код и таким образом обрабатывает всё быстро без особых нагрузок.
"""


def huffman(string):

    count = Counter(string).most_common()[::-1]
    codes = {}
    left = "0"
    right = "1"

    if len(count) == 0:
        return "Пустая строка"

    elif len(count) < 4:
        if len(count) == 3:
            codes[count.pop()[0]] = right + "1"
            codes[count.pop()[0]] = left
            codes[count.pop()[0]] = right + "0"
            return codes
        else:
            try:
                codes[count.pop()[0]] = right
                codes[count.pop()[0]] = left
                return codes
            except:
                return codes

    else:
        while len(count) > 4:
            codes[count.pop()[0]] = right + "1"
            right += "0"

            codes[count.pop()[0]] = left + "0"
            left += "1"

        if len(count) == 4:
            codes[count.pop()[0]] = right + "1"
            codes[count.pop()[0]] = right + "0"
            codes[count.pop()[0]] = left + "0"
            codes[count.pop()[0]] = left + "1"

        else:
            codes[count.pop()[0]] = right + "1"
            codes[count.pop()[0]] = left
            codes[count.pop()[0]] = right + "0"

        return codes


string = input("Введите строку: ")
codes = huffman(string)
print(f'Кодировки символов: {codes}')
print('Закодированная строка:')
for sym in string:
    print(codes[sym], end=" ")
