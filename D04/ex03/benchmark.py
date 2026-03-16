import sys
import timeit
from functools import reduce

def loop(n):
    summ = 0
    for i in range(1, n + 1):
        summ += i * i
    return summ

def red(n):
    return reduce(lambda x, y: x + y * y, range(1, n + 1), 0)


if __name__ == '__main__':
    try:
        if len(sys.argv) != 4:
            raise Exception('Должно быть 4 аргумента: benchmark.py, loop/red, количество вызовов, число!')

        try:
            number_of_calls = int(sys.argv[2])
            n = int(sys.argv[3])
        except:
            raise Exception('Третий и четвертый аргументы должны быть числом!')

        if sys.argv[1] == 'loop':
            timeit_t = timeit.timeit(lambda: loop(n), number=number_of_calls)
        elif sys.argv[1] == 'red':
            timeit_t = timeit.timeit(lambda: red(n), number=number_of_calls)
        else:
            raise Exception('Второй аргумент: loop/red')

        print(timeit_t)

    except Exception as e:
        print(e)

    

