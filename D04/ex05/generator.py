import sys
import time
import resource

def read_file_gen(path):
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            yield line  # возвращаем по одной строке

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Укажите путь к файлу ratings.csv")
        sys.exit(1)

    path = sys.argv[1]

    start = time.time()
    for line in read_file_gen(path):
        pass
    end = time.time()

    usage = resource.getrusage(resource.RUSAGE_SELF)
    peak_memory_gb = usage.ru_maxrss / 1024 / 1024  # ГБ

    total_cpu_time = usage.ru_utime + usage.ru_stime

    print(f"Peak Memory Usage = {peak_memory_gb:.3f} GB")
    print(f"User Mode Time + System Mode Time = {total_cpu_time:.2f}s")
