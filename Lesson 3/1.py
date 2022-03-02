num_dict = dict.fromkeys(range(2, 10), 0)

for num in range(2, 100):
    for i in range(2, 10):
        if num % i == 0:
            num_dict[i] += 1

for key in num_dict:
    print(f'{num_dict[key]} кратны {key}')