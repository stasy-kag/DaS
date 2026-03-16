import timeit
import random
from collections import Counter

def count_dict(data):
    d = {i: 0 for i in range(101)}
    for num in data:
        d[num] += 1
    return d

def top10_dict(data):
    d = count_dict(data)
    d_sorted = sorted(d.items(), key = lambda x: x[1], reverse = True)[0:10]
    return d_sorted

def count_counter(data):
    return dict(Counter(data))


def top10_counter(data):
    return Counter(data).most_common(10)

if __name__ == '__main__':
    data = [random.randint(0,100) for _ in range(1,1_000_000)]

    t_count_dict = timeit.timeit(lambda: count_dict(data), number=1)
    t_count_counter = timeit.timeit(lambda: count_counter(data), number=1)

    t_top10_dict = timeit.timeit(lambda: top10_dict(data), number=1)
    t_top10_counter = timeit.timeit(lambda: top10_counter(data), number=1)

    print(f"my function: {t_count_dict:.7f}")
    print(f"Counter: {t_count_counter:.7f}")

    print(f"my top: {t_top10_dict:.7f}")
    print(f"Counter's top: {t_top10_counter:.7f}")