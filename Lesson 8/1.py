import hashlib


def all_substr(S):
    h_lst = []
    s_lst = []
    n = len(S)

    for len_sub in range(1, n):
        for i in range(n - len_sub + 1):
            h_sub = hashlib.sha1(S[i:i + len_sub].encode('utf-8')).hexdigest()
            if h_sub not in h_lst:
                h_lst.append(h_sub)
                s_lst.append(S[i:i + len_sub])

    if len(s_lst) > 0:
        return f'В строке "{S}" найдено {len(s_lst)} уникальных подстрок: \n{s_lst}'
    return 'Пустая строка'


S = input('Введите строку: ')
print(all_substr(S))
