from random import randint
from collections import Counter

num_list = [randint(1, 5) for _ in range(10)]

counter = Counter(num_list)

print(f'В списке \n{num_list} \nчаще всего встречается число:'
      f' {max(counter, key=counter.get)} ({counter[max(counter, key=counter.get)]}) раз)')
