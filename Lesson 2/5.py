cut = 1
for i in range(32, 128):
    if i == 128:
        print(f'{i}   {chr(i)}', end="")
    if cut % 10 == 0:
        print(f'{i}   {chr(i)}', end="\n")
    else:
        print(f'{i}   {chr(i)}', end= "\t")
    cut += 1