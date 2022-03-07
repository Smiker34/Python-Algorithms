import timeit
import cProfile

n = int(input('Какое по счету простое число вы хотите найти: '))
nums = [i for i in range(n * n)]


def simple(num_list, idx):
    num_list[1] = 0
    s_nums = []
    for i in range(2, len(num_list)):
        for num in s_nums:
            if num_list[i] % num == 0:
                break
        else:
            s_nums.append(num_list[i])
        if len(s_nums) == idx:
            return s_nums[-1]


def sieve(num_list, idx):
    num_list[1] = 0
    i = 2
    s_num_list = []
    length = 0
    length_num_list = len(num_list)
    while length < idx:
        if num_list[i] != 0:
            s_num_list.append(num_list[i])
            length += 1
            j = i * 2
            while j < length_num_list:
                num_list[j] = 0
                j += i
        i += 1
    return s_num_list[-1]

start_time = timeit.default_timer()
print(simple(nums, n))
print(timeit.default_timer() - start_time)
cProfile.run('simple(nums, n)')
'''
Время при n = 3: 2.6900000000162905e-05
Время при n = 30: 9.480000000028355e-05
Время при n = 300: 0.004786600000000085
Время при n = 3000: 0.4428207999999998

Результаты профайлера с n = 3000:

         30453 function calls in 0.448 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.448    0.448 <string>:1(<module>)
        1    0.445    0.445    0.448    0.448 main.py:8(simple)
        1    0.000    0.000    0.448    0.448 {built-in method builtins.exec}
    27449    0.003    0.000    0.003    0.000 {built-in method builtins.len}
     3000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
start_time = timeit.default_timer()
print(sieve(nums, n))
print(timeit.default_timer() - start_time)
cProfile.run('sieve(nums, n)')
'''
Время при n = 3: 9.799999999948739e-06
Время при n = 30: 0.00024629999999969954
Время при n = 300: 0.030711500000000225
Время при n = 3000: 3.8750655

Результаты профайлера с n = 3000:

         3005 function calls in 3.369 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.369    3.369 <string>:1(<module>)
        1    3.368    3.368    3.369    3.369 main.py:21(sieve)
        1    0.000    0.000    3.369    3.369 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     3000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

'''
Сложность обоих способов O(n^2)
Вычисление через решето значительно медленнее.
'''
